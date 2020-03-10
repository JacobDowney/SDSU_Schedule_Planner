# VERY EXPENSIVE OPERATION
# ------------------------
# Gets a dictionary of all courses with their information
# Gets an abbreviation for each subject and goes through the list.
# For each abbr it scraps the information for the courses under the abbr.
# It takes that information and adds it to courses.
def get_dict_of_all_courses():
    abbrs = get_abbr_of_all_subjects()
    courses = []
    for abbr in abbrs:
        url = get_course_url(abbrev = abbr)
        odd_courses = scrap_info_from_url(url, "sectionRecordOdd")
        even_courses = scrap_info_from_url(url, "sectionRecordEven")
        reformatted_courses = reformat_courses(odd_courses) + reformat_courses(even_courses)
        for course in reformatted_courses:
            courses.append(course)
    return courses


# VERY EXPENSIVE OPERATION
# ------------------------
# Much like get_dict_of_all_courses() but only returns a list of sched numbers.
# Goes through the same algorithms but only stores sched numbers.
def get_list_schedule_numbers():
    courses = get_dict_of_all_courses()
    sched_nums = []
    for course in courses:
        sched_nums.append(sched)

    abbrs = get_abbr_of_all_subjects()
    """
    sched_nums = []
    for abbr in abbrs:
        url = get_course_url(abbrev = abbr)
        odd_courses = scrap_info_from_url(url, "sectionRecordOdd")
        even_courses = scrap_info_from_url(url, "sectionRecordEven")
        reformatted_sched_num = reformat_sched_nums(odd_courses) + reformat_sched_nums(even_courses)
        for sched_num in reformatted_sched_num:
            sched_nums.append(sched_num)
    return sched_nums
    """


# Returns array of dictionaries with different course infos
def get_dict_of_course_info_from_title(course_title):
    url = get_course_url(title = course_title)
    odd_courses = scrap_info_from_url(url, "sectionRecordOdd")
    even_courses = scrap_info_from_url(url, "sectionRecordEven")
    return reformat_courses(odd_courses) + reformat_courses(even_courses)

# Returns array of dictionaries with different course infos
def course_info(abbr, num):
    abbr.replace(" ", "+")
    url = get_course_url(abbrev = abbr, number = num)
    odd_courses = scrap_info_from_url(url, "sectionRecordOdd")
    even_courses = scrap_info_from_url(url, "sectionRecordEven")
    return reformat_courses(odd_courses) + reformat_courses(even_courses)


# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                               PRIVATE METHODS                                #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #



# Returns a dictionary of all the course information from a courses html
# Each dictionary contains a list for certain data with multiple options
def reformat_courses(courses):
    course_info = []
    for course in courses:
        sched = course.find_all("div", {"class": "sectionFieldSched column"})[0].text.strip()
        title = course.find_all("div", {"class": "sectionFieldTitle column"})[0].text.strip()
        if sched != "*****" and title != "":
            temp_name = course.find_all("div", {"class": "sectionFieldCourse column"})[0].text.strip().split('-')
            name = temp_name[0]
            number = temp_name[1]
            units = course.find_all("div", {"class": "sectionFieldUnits column"})[0].text.strip()

            formats = []
            formats_list = course.find_all("div", {"class": "sectionFieldType column"})
            for format in formats_list:
                format = format.text.strip()
                if len(format) != 0:
                    formats.append(format)

            times = []
            times_list = course.find_all("div", {"class": "sectionFieldTime column"})
            for time in times_list:
                time = time.text.strip()
                if len(time) != 0:
                    times.append(time)

            days = []
            days_list = course.find_all("div", {"class": "sectionFieldDay column"})
            for day in days_list:
                day = day.text.strip()
                if len(day) != 0:
                    days.append(day)

            locations = []
            locations_list = course.find_all("div", {"class": "sectionFieldLocation column"})
            for location in locations_list:
                location = location.text.strip()
                if len(location) != 0:
                    locations.append(location)

            professors = []
            professors_list = course.find_all("div", {"class": "sectionFieldInstructor column"})
            for professor in professors_list:
                professor = professor.text.strip()
                if len(professor) != 0:
                    professors.append(professor)

            seats_open = course.find_all("div", {"class": "sectionFieldSeats column"})[0].text.strip()
            course_info.append({'name': name,
                                'number': number,
                                'sched': sched,
                                'title': title,
                                'units': units,
                                'formats': formats,
                                'times': times,
                                'days': days,
                                'locations': locations,
                                'professors': professors,
                                'seats_open': seats_open})
    return course_info
