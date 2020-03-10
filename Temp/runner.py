from collections import defaultdict
import Planner

def print_sorted_class_sizes():
    dict_of_course_sizes = defaultdict(int)
    abbrs = Planner.get_abbr_of_all_subjects()
    for abbr in abbrs:
        courses = SchedulePlanner.get_dict_of_course_info_from_subject(abbr)
        for course in courses:
            total = int(course['seats_open'].split('/')[1].split('W')[0])
            dict_of_course_sizes[total] += 1
    for key in sorted(dict_of_course_sizes.iterkeys()):
        print "%s: %s" % (key, dict_of_course_sizes[key])


def check_multiple_professors():
    courses = Planner.course_info("TFM", "160")
    for course in courses:
        print course['title']
        print course['sched']
        print course['professors']
        print ""

def test_simple_scrap():
    courses = Planner.course_info("OCEAN", "100")
    print ""
    print courses

def main():
    test_simple_scrap()



if __name__ == '__main__':
    main()
else:
    print "Not Supported"
