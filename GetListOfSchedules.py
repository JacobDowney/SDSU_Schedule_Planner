# NOTE AS OF 5/3/2020
# THIS IS CORRECT EXCEPT FOR DATABASE CALLS
#
# THIS IS ASSUMING EVERY COURSE THAT IS AN INPUT AS COURSES FOR GET_LIST_OF_SCHEDULES
# IS GOING TO BE USED TO CREATE THAT FINAL SCHEDULE.

# Example:
# course_names = [
#       (CS, 108), ->    ids: a, b, c
#       (STAT, 550), ->  ids: d, e
#       (MATH, 245) ] -> ids: f, g, h
"""
Given a list of courses, returns the list of all possible schedules with those
course names.
:param courses: A list of tuples containing (subject, number) pairs for a given
                course.
:return: A list of schedules, each schedule containing a list of main_ids
:rtype: A list of list of main_ids
"""
def get_list_of_schedules(courses):
    course_main_ids = []
    for course in courses:
        course_main_ids.append(get_main_ids(course))
    return get_schedules([], [], course_main_ids)


### TODO WORK ON DATABASE CALL
"""
Given a specific course, returns a list of all main_ids for that class.
:param course: A course is a tuple that contains (subject, number)
:return: A list of all main_ids for that given course
:rtype: A list of main_ids
"""
def get_main_ids(course):
    course_subject = course[0]
    course_num = course[1]
    # Call database and get list of main ids for the course name
    return None


"""
A recursive function that takes in the schedules that have already been created,
the current schedule that is being creted, and the remaining courses for the
schedule that is being made
:param schedules:
:param current_schedule:
:param remaining_courses:
:return: A list of schedules, each schedule containing a list of id numbers
:rtype: A list of lists of id numbers
"""
def get_schedules(schedules, current_schedule, remaining_courses):
    if len(remaining_courses) == 0:
        current_schedule.sort()
        if not_in_schedules(schedules, current_schedule):  # Why would this already be in there???
            schedules.append(current_schedule)
        return schedules

    ids = remaining_courses[0]
    for id in ids:
        if fits_in_schedule(current_schedule, id):
            updated_schedule = current_schedule[:]
            updated_schedule.append(id)
            schedules = get_schedules(schedules, updated_schedule, remaining_courses[1:])
    return schedules


### TODO: OPTIMIZE sort courses by times & binary search if the course would fit
# Goes through all the current ids and if the id can fit for each current_id
# then return True. If there is an id it doesn't work with, then return False
def fits_in_schedule(current_schedule, id):
    for current_id in current_schedule:
        if overlap(current_id, id):
            return False
    return True


### TODO: Database calls
# Returns false if there is no overlap, and true if there is an overlap
def overlap(current_id, id):
    current_start = 0
    current_end = 1
    start = 2
    end = 3
    return (in_between(current_start, current_end, start) or in_between(start, end, current_start))

# Returns true if insert is in between start and end
def in_between(start, end, insert):
    return insert >= start and insert <= end

# Return true if current_ids are not in schedules and we should add them
def not_in_schedules(schedules, current_schedule):
    for schedule in schedules:
        match = True
        for schedule_id, current_id in zip(schedule, current_schedule):
            if schedule_id != current_id:
                match = False
                break
        if match:
            return False
    return True


# holder
