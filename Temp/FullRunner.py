import SDSUPlanner
import RateMyProf
import printer
import json
from operator import itemgetter

LIST_OF_SECTIONS = [
        "american_history", #0
        "united_states_constitution", #1
        "californina_government", #2
        "oral_communication", #3
        "composition", #4
        "intermediate_composition", #5
        "physical_sciences", #6 NOT WORKING
        "life_sciences", #7
        "science_lab", #8
        "math", #9
        "foundations_social_sciences", #10
        "literature", #11
        "art_classics_dance_music", #12
        "history", #13
        "philosophy", #14
        "foreign_language", #15 NOT FILLED
        "explorations_natural_sciences", #16 NOT WORKING
        "explorations_social_sciences", #17
        "explorations_humanities" #18 NOT WORKING
]

# TODO check professors name before searching rate my professor
def main():
    degree_eval = ""
    with open('degree.json') as file:
        degree_eval = json.load(file)
    list_courses = degree_eval['degree_evaluation']['requirements'][LIST_OF_SECTIONS[18]]

    courses = []

    print "OPENED EVAL JSON"
    print "STARTING SDSU WEB PORTAL SCRAP AND REFORMATTING"

    """
    for section in list_courses:
        subject = section['subject']
        numbers = section['numbers']
        for number in numbers:
            courses += SDSUPlanner.course_info(subject, number)
    """
    courses += SDSUPlanner.course_info("RWS", "305")

    main_info = []

    print "STARTING PROFESSOR SCRAP"

    stored_professor_info = {}

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
                if professor_info['first_name'][0] == professor[0]:
                    list_possible.append(professor_info['overall_quality'])
                    found = True
            if not found:
                print "ERROR: PROFESSOR " + professor + " NOT FOUND"
                continue

            # iterate through and average professor scores
            total = 0
            for possible in list_possible:
                total += float(possible)
            total /= len(list_possible)

            test_tuple = (total, printer.get_course_str(course, professor_infos[0]))
            main_info.append(test_tuple)


    main_info.sort(key=itemgetter(0), reverse=True)

    for tuple in main_info:
        print tuple[1]
        print tuple[0]
        print ""





if __name__ == '__main__':
    main()
else:
    print "Not Supported"
