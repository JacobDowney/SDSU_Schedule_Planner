
# course_names = [
#       {subject : subject, number : number},
#       {...}, {...}, ...]
def get_list_of_schedules(course_names):
    course_main_ids = []
    for course_name in course_names:
        main_ids = get_main_ids(course_name)
        course_main_ids.append(main_ids)

    return get_schedules([], [], course_main_ids)

# Returns a list of main id for that specific course_name
def get_main_ids(course_name):
    # Call database and get list of main ids for the course name
    return None

# Recursive function
def get_schedules(schedules, current_ids, remaining_courses):
    if len(remaining_courses) == 0:
        current_ids.sort()
        if not_in_schedules(schedules, current_ids):
            schedules.append(current_ids)
        return schedules
    ids = remaining_courses[0]
    for id in ids:
        if fits_in_schedule(current_ids, id):
            new_current_ids = current_ids[:]
            new_current_ids.append(id)
            new_remaining_courses = remaining_courses[1:]
            schedules = get_schedules(schedules, new_current_ids, new_remaining_courses)
    return schedules

# Goes through all the current ids and if the id can fit for each current_id
# then return True. If there is an id it doesn't work with, then return False
def fits_in_schedule(current_ids, id):
    for current_id in current_ids:
        if id not in current_id:
            return False
    return True

# Return true if current_ids are not in schedules and we should add them
def not_in_schedules(schedules, current_ids):
    for schedule in schedules:
        match = True
        for schedule_id, current_id in zip(schedule, current_ids):
            if schedule_id != current_id:
                match = False
                break
        if match:
            return False
    return True

"""
1.) Input is a list of courses that are dictionaries
        - each course has a subject and number
2.) Gets a list of lists
3.) Function that takes in:
        - a list of current courses that are apart of the schedule, a list of remaining course_dictionaries
        courses,
"""
