import json
import SDSUWebPortalCourseInfo
from SchedUrls import sched_urls

def main():
    sdsu_webportal_course_info = SDSUWebPortalCourseInfo.get_sdsu_webportal_course_info(sched_urls)
    with open('SDSUCourseInfo.json', "w") as sdsu_course_info_json:
        json.dump(sdsu_webportal_course_info, sdsu_course_info_json)

if __name__ == '__main__':
    main()
else:
    print "Not Supported"
