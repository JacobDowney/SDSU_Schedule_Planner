import requests
import re
import SDSUPlanner
from bs4 import BeautifulSoup
from collections import defaultdict

FINAL_PERIOD = "20202"
FINAL_SCHED_URL_START = "https://sunspot.sdsu.edu/schedule/"

# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                           TOP LEVEL METHOD                                   #
# ---------------------------------------------------------------------------- #
# Returns a dictionary of three different information necesary for setting up  #
# an sql database.                                                             #
#   1.) Key: 'course_infos'                                                    #
#       Value: A list of course infos for all courses.                         #
#   2.) Key: 'meeting_dict'                                                    #
#       Value: A dictionary of (five digit numeric numbers -> meetings)        #
#   3.) Key: 'footnote_dict'                                                   #
#       Value: A dictionary of (footnote codes -> footnote DETAILS)            #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def get_sdsu_webportal_course_info(urls):
    # Gets a list of all the subjects
    # course_subjects = SDSUPlanner.get_all_subjects()
    progress("Get all subjects", 1, 5)

    # Goes through all the subjects and gets all the url endings
    # url_endings = get_all_url_endings(course_subjects, period=FINAL_PERIOD)
    progress("Get all url endings", 2, 5)

    # Getting the raw course infos
    raw_course_infos = get_raw_course_infos(urls)
    progress("Get raw course info", 3, 5)

    # Filling meeting and footnote dictionaries
    meeting_dict, footnote_dict, course_infos = get_all_course_infos(raw_course_infos)
    progress("Get course infos", 4, 5)

    # Setting up the sdsu_webportal_course_info and reversing the meeting_dict
    sdsu_webportal_course_info = {
        'course_infos': course_infos,
        'meeting_dict': dict(reversed(item) for item in meeting_dict.items()),
        'footnote_dict': footnote_dict
    }
    progress("Composed sdsu_webportal_course_info dictionary", 5, 5)

    return sdsu_webportal_course_info



# helpers in order

def get_all_url_endings(subjects):
    url_endings = []
    for subject in subjects:
        subject_url = SDSUPlanner.get_course_url(abbrev = subject)
        new_url_endings = SDSUPlanner.get_url_endings(subject_url)
        for url_ending in new_url_endings:
            url_endings.append(url_ending)
    return url_endings

def get_raw_course_infos(urls):
    raw_course_infos = []
    for url in urls:
        raw_course_info = SDSUPlanner.get_raw_course_info(url)
        if not raw_course_info:
            raw_course_infos.append(raw_course_info)
    return raw_course_infos

def get_all_course_infos(raw_course_infos):
    meeting_dict = {}
    footnote_dict = {}
    course_infos = []
    counter = 10000
    for raw_course_info in raw_course_infos:
        meetings = get_meetings(raw_course_info)
        for meeting in meetings:
            if meeting not in meeting_dict:
                counter += 1
                meeting_dict[meeting] = counter

        footnotes = get_footnotes(raw_course_info)
        for footnote in footnotes:
            code = footnote['code']
            if code not in footnote_dict:
                footnote_dict[code] = footnote['detail']

        course_info = get_course_info(raw_course_info, meeting_dict, meetings, footnotes)
        course_infos.append(course_info)

    return meeting_dict, footnote_dict, course_infos


################################################################################

# Returns a list of meeting dictionaries
def get_meetings(raw_course_info):
    raw_meetings = raw_course_info.get("Meetings")
    meetings = []
    if raw_meetings:
        types = raw_meetings.find_all("div", {"class": "sectionFieldType column"})
        times = raw_meetings.find_all("div", {"class": "sectionFieldTime column"})
        days = raw_meetings.find_all("div", {"class", "sectionFieldDay column"})
        locations = raw_meetings.find_all("div", {"class", "sectionFieldLocation column"})
        instructors = raw_meetings.find_all("div", {"class", "sectionFieldInstructor column"})
        length = len(types)
        if any(len(list) != length for list in [times, days, locations, instructors]):
            print "ERROR LENGTHS NOT EQUIVALENT!!!"
        for type, time, day, location, instructor in zip(types, times, days, locations, instructors):
            meeting = {
                'type': type.text.strip(),
                'time': time.text.strip(),
                'day': day.text.strip(),
                'locations': location.a.text.strip(),
                'instructor': instructor.a.text.strip()
            }
            meetings.append(meeting)
    return meetings

# Returns a list of footnote dictionaries
def get_footnotes(raw_course_info):
    raw_footnotes = raw_course_info['Footnotes']
    codes = raw_footnotes.find_all("div", {"class": "footnoteCode column"})
    details = raw_footnotes.find_all("div", {"class": "footnoteDetails column"})
    footnotes = []
    if (len(codes) != len(details)):
        print "ERROR: Length of footnote codes != length of footnote details"
    for code, detail in zip(codes, details):
        footnote = {
            'code': code.text.strip(),
            'detail': detail.text.strip()
        }
        footnotes.append(footnote)
    return footnotes

################################################################################


def get_course_info(raw_course_info, meeting_dict, meetings, footnotes):
    course_name = raw_course_info['Course'].text.strip().split("-")
    course_info = {
        'subject': course_name[0].replace(" ", "+"),
        'number': course_name[1],
        'title': get_course_info_stripped(raw_course_info, 'Course Title'),
        'section': get_course_info_stripped(raw_course_info, 'Section'),
        'sched_num': get_course_info_stripped(raw_course_info, 'Schedule #'),
        'units': get_course_info_stripped(raw_course_info, 'Units'),
        'session': get_course_info_stripped(raw_course_info, 'Session'),
        'seats_open': get_course_info_stripped(raw_course_info, 'Seats'),
        'meetings': get_meeting_dict_keys(meetings, meeting_dict),
        'full_title': get_course_info_stripped(raw_course_info, 'Full Title'),
        'description': get_course_info_stripped(raw_course_info, 'Description'),
        'prerequisite': get_course_info_stripped(raw_course_info, 'Prerequisite'),
        'statement': get_course_info_stripped(raw_course_info, 'Statement'),
        'footnotes': get_footnote_codes(footnotes)
    }
    return course

################################################################################

# If the key doesn't exist it returns None but if the key exists it returns the
# stripped text value for that key
def get_course_info_stripped(course_info, key):
    value = course_info.get(key)
    if value:
        return value.text.strip()
    return None

# Returns a list of values from the meeting dict
def get_meeting_dict_keys(meetings, meeting_dict):
    keys = []
    for meeting in meetings:
        key = meeting_dict.get(meeting)
        if key:
            keys.append(key)
        else:
            print "ERROR MEETING DOESN'T EXIST IN MEETING DICTIONARY"
    return keys


# Returns a list of footnote codes for a given course_info
def get_footnote_codes(footnotes):
    footnote_codes = []
    for footnote in footnotes:
        footnote_codes.append(footnote['code'])
    return footnote_codes

################################################################################
def progress(message, num, total):
    print("COMPLETE: {0} - ({1}/{2})".format(message, num, total))


#holder
