import SDSUWebPortalCourseInfo
import SDSUPlanner
from SchedUrls import sched_urls

FINAL_SCHED_URL_START = "https://sunspot.sdsu.edu/schedule/"

def main():
    get_courses()
    #print_sched_urls()

def get_courses():
    courses = SDSUWebPortalCourseInfo.get_sdsu_webportal_course_info(sched_urls)

    print "\n=========================\n\n"
    print courses['course_infos'] + "\n"
    print courses['meeting_dict'] + "\n"
    print courses['footnote_dict'] + "\n"

def print_sched_urls():
    course_subjects = SDSUPlanner.get_all_subjects()
    SDSUWebPortalCourseInfo.progress("Get all subjects", 1, 5)
    url_endings = SDSUWebPortalCourseInfo.get_all_url_endings(course_subjects)
    SDSUWebPortalCourseInfo.progress("Get all url endings", 2, 5)

    course_urls = []
    for url_ending in url_endings:
        course_url = FINAL_SCHED_URL_START + url_ending
        course_urls.append(course_url)
    print course_urls

if __name__ == '__main__':
    main()
else:
    print "Not Supported"
