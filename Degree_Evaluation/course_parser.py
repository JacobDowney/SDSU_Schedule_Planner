from degree_evaluation import Course
import re

"""
PUBLIC TOP LEVEL METHOD
Params: String raw_course_list
Returns: list of Course objects from degree_evaluation.py
"""
def get_list_of_courses(raw_course_list):
    raw_course_list = raw_course_list.strip()
    subject_ranges = get_subject_ranges(raw_course_list)
    courses = []
    for subject_range in subject_ranges:
        courses_for_subject_range = get_courses_from_subject_range(subject_range, raw_course_list)
        for course in courses_for_subject_range:
            courses.append(course)
    for course in courses:
        print "%s: %s" % (course.subject, course.number)
    print len(courses)

# TODO: Find how to do regex with 2 or more
# TODO: If a subject goes to a new line it prints the subject again
"""
Params: String raw_course_list
Returns: A list of dictionaries containing a 'name' and 'range'.
        [{'name': 'AFRAS', 'range': (5, 43)}, ...]
"""
def get_subject_ranges(raw_course_list):
    # This complicated regex is basically saying:
    # Either 'A E', 'A S', 'B A', or any other less then five characters
    # CAN IMPROVE::: POSSIBLY MAKE JUST A OR LIST OF ALL THE SUBJECTS
    pattern = r'A\sE|A\sS|B\sA|[A-Z]{2}[A-Z\s]{,2}[A-Z]?|[C-Z][A-Z\s]{1,3}[A-Z]'
    regex = re.compile(pattern)
    matches = regex.finditer(raw_course_list)

    subject_ranges = []
    ending_index = -1
    previous_match_name = ""
    for match in matches:
        if (ending_index != -1):
            dict_subject_range = {
                'name': previous_match_name,
                'range': (ending_index, match.span()[0])
            }
            subject_ranges.append(dict_subject_range)
        previous_match_name = match.group(0).strip()
        ending_index = match.span()[1]
    dict_last_subject_range = {
        'name': previous_match_name,
        'range': (ending_index, len(raw_course_list))
    }
    subject_ranges.append(dict_last_subject_range)
    return subject_ranges

"""
Params: Dictionary subject_range - {'name': 'AFRAS', 'range': (5, 43)}
Returns: A list of Course objects from degree_evaluation.py
"""
def get_courses_from_subject_range(subject_range, raw_course_list):
    courses = []
    name = subject_range['name']
    range = subject_range['range']
    if (len(name) > 5):
        error("SUBJECT NAME CANNOT BE OVER 5, IT'S: %s" % (name))
    numbers = raw_course_list[range[0]:range[1]].split(',')
    for number in numbers:
        number = number.strip()
        if (len(number) != 0):
            course_params = {'subject': name, 'number': number}
            courses.append(Course(course_params))
    return courses

# Error handler
def error(error):
    print "ERROR: " + error

get_list_of_courses(test_course_info)
