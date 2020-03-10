import Planner

courses = Planner.get_dict_of_all_courses()

#print courses

infos = {}

for course in courses:
    abbr = course['name']
    professors = course['professors']
    for professor in professors:
        if professor not in infos:
            infos[professor] = []
        if abbr not in infos[professor]:
            infos[professor].append(abbr)

for key, value in infos.items():
    if len(value) > 1:
        print key
        print value
        print ""
    
