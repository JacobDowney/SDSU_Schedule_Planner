import SDSUPlanner
import RateMyProf
import printer
import time
import json
from operator import itemgetter

SECTION = "history"

# TODO check professors name before searching rate my professor
def main():

    print "STARTING SDSU WEB PORTAL SCRAP AND REFORMATTING"
    start = time.time()

    #courses = SDSUPlanner.get_dict_of_all_courses()
    courses = SDSUPlanner.course_info("RWS", "100")

    end = time.time()
    print "FINISHED SDSU WEB PORTAL SCRAP AND REFORMATTING"
    print "TIME ELAPSED: " + str(end - start) + " SECONDS."


    print "STARTING PROFESSOR SCRAP"
    start = time.time()

    main_info = []

    for course in courses:
        professors = course['professors']
        for professor in professors:
            first_letter = professor[0]
            last_name = professor[3:]
            professor_infos = RateMyProf.get_all_professors_info(first_letter, last_name)

            found = False
            list_possible = []
            for professor_info in professor_infos:
                if len(professor_info['first_name']) == 0 or len(professor) == 0:
                    continue
                if professor_info['first_name'][0] == first_letter:
                    list_possible.append(professor_info)
                    found = True

            if not found:
                print "ERROR: PROFESSOR " + professor + " NOT FOUND\n"
                continue

            if len(list_possible) != 1:
                print "possibles are:"
                for possible in list_possible:
                    print printer.get_rate_my_prof_info(possible)
                print "done with possibles\n"

            #test_tuple = (total, printer.get_course_str(course, professor_infos[0]))
            #main_info.append(test_tuple)

    """
    main_info.sort(key=itemgetter(0), reverse=True)

    for tuple in main_info:
        print tuple[1]
        print tuple[0]
        print ""
    """





if __name__ == '__main__':
    main()
else:
    print "Not Supported"
