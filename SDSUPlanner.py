import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict

FINAL_MODE = "search"
FINAL_PERIOD = "20202"
FINAL_ADMIN_UNIT = "R"

FINAL_SEARCH_LINK = "https://sunspot.sdsu.edu/schedule/search"


# Returns an array of all the subject abbreviations
def get_all_subjects():
    soup = BeautifulSoup(requests.get(FINAL_SEARCH_LINK).content, "html.parser")
    raw_subjects = soup.find_all("select", {"class": "requiredField column"})[0].find_all("option")
    subjects = []
    for i in range(3, len(raw_subjects)):
        subject = str(raw_subjects[i].text.replace(u'\xa0', u' '))[0:5].strip().replace(u' ', u'+')
        subjects.append(subject)
    return subjects



#------------------------------------------------------------------------------#
#                Returns a course url from the given parameters                #
# ---------------------------------------------------------------------------- #
# url = 'https://sunspot.sdsu.edu/schedule/search?mode=&period=&admin_unit='   #
#       + '&abbrev=&number=&suffix=&courseTitle=&scheduleNumber=&units='       #
#       + '&instructor=&facility=&space=&meetingType=&startHours=&startMins='  #
#       + '&endHours=&endMins=&remaining_seats_at_least=&ge='                  #
#------------------------------------------------------------------------------#
def get_course_url(mode=FINAL_MODE, period=FINAL_PERIOD,
                    admin_unit=FINAL_ADMIN_UNIT, abbrev="", number="",
                    suffix="", title="", sched="", units="", instructor="",
                    facility="", space="", meeting_type="", start_hours="",
                    start_mins="", end_hours="", end_mins="",
                    remaining_seats_at_least="", ge=""):
    url = ('https://sunspot.sdsu.edu/schedule/search?mode=' + mode + '&period='
            + period + '&admin_unit=' + admin_unit + '&abbrev=' + abbrev
            + '&number=' + number + '&suffix=' + suffix + '&courseTitle='
            + title + '&scheduleNumber=' + sched + '&units=' + units
            + '&instructor=' + instructor + '&facility=' + facility + '&space='
            + space + '&meetingType=' + meeting_type + '&startHours='
            + start_hours + '&startMins=' + start_mins + '&endHours='
            + end_hours + '&endMins=' + end_mins + '&remaining_seats_at_least='
            + remaining_seats_at_least + '&ge=' + ge)
    return url

#------------------------------------------------------------------------------#
#  Returns a dictionary for scraped course information for a given course url  #
# ---------------------------------------------------------------------------- #
# Key: Label - Stripped text representing the label.                           #
#         EX - Course, Section, Seats...                                       #
# Value: Content - The unstripped content that is still in soup format to      #
#                  search and find different parts. In HTML format to continue #
#                  to use soup methogs like find_all on it.                    #
#         EX - AACTG-326, 01, 26/30...                                         #
#------------------------------------------------------------------------------#
def get_raw_course_info(course_url):

    soup = BeautifulSoup(requests.get(course_url).content, "html.parser")
    scraped_info = soup.find_all("table", {"id": "sectionDetailTable"})
    raw_course_info = {}
    if len(scraped_info) < 1:
        print course_url
    else:
        contents = scraped_info[0].find_all("tr")
        for content in contents:
            label = content.find_all("td", {"class": "sectionDetailLabel"})[0].text.strip()
            content = content.find_all("td", {"class": "sectionDetailContent"})[0]
            raw_course_info[label] = content
    return raw_course_info



# TODO: FINISH THIS TO CHECK IF ITS THERE
# THIS MIGHT NOT WORK
def get_url_endings(subject_url):
    soup = BeautifulSoup(requests.get(subject_url).content, "html.parser")
    raw_url_endings = soup.find_all("div", {"class": "sectionFieldCourse column"})
    url_endings = []
    for raw_url_ending in raw_url_endings:
        if raw_url_ending.a:
            url_ending = raw_url_ending.a.get('href')
            url_endings.append(url_ending)
    return url_endings
