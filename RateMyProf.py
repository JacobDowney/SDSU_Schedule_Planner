import requests
from bs4 import BeautifulSoup

FINAL_QUERY_OPTION = "HEADER"
FINAL_SCHOOL_NAME = "San+Diego+State+University"
FINAL_SCHOOL_ID = "877"

FINAL_RATE_MY_PROFESSOR_URL = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid="

# TOP LEVEL METHOD
# ----------------
#
def get_all_professors_info(first_letter, last_name):
    ids = get_professor_ids(first_letter, last_name)
    professor_infos = []
    for id in ids:
        professor_info = get_professor_info(id)
        if professor_info != None:
            professor_infos.append(professor_info)
    if len(professor_infos) == 0:
        print "RATEMYPROF ERROR: NO PROFESSOR INFO FOR: " + first_letter + " " + last_name
    return professor_infos

# Returns a list of professor id's for a given professor name.
# ------------------------------------------------------------
# Example: For professor name: P, Kraft there would first be 3 professors:
# Brenna Kraft, Heidi Kraft, and Patty Kraft. Given that only Patty Kraft has a
# first name that starts with P, the list being returned would be:
# [96810]
def get_professor_ids(first_letter, last_name):
    url = get_prof_id_url(query_by = "teacherName", query = last_name)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    infos = soup.find_all("li", {"class": "listing PROFESSOR"})
    names = soup.find_all("span", {"class": "main"})
    ids = []
    if len(names) != len(infos):
        print "RATEMYPROF ERROR: NOT EQUAL LENGTH OF INFOS AND NAMES"
    for (info, name) in zip(infos, names):
        if (first_letter == name.text.split(",")[1].strip()[0]):
            ids.append(str(info)[61:70].split('"')[0])
    return ids

# Returns a url for a rate my professor query from San Diego State with a
# specific professor name as the query parameter being queried by the professor
# name.
def get_prof_id_url(query_option = FINAL_QUERY_OPTION, query_by = "",
                    school_name = FINAL_SCHOOL_NAME,
                    school_id = FINAL_SCHOOL_ID, query = ""):
    url = ('http://www.ratemyprofessors.com/search.jsp?queryoption='
            + query_option + '&queryBy=' + query_by + '&schoolName='
            + school_name + '&schoolID=' + school_id + '&query=' + query)
    return url

# Given a professor id, returns a diection of professor info containing a
# professor's: {first_name, last_name, department, overall_quality,
# would_take_again, level_of_difficulty}
# TODO: make department into a regex expression
def get_professor_info(id):
    url = FINAL_RATE_MY_PROFESSOR_URL + id
    if len(scrap_info_from_url(url, "div", "rating-breakdown")) == 0:
        return None
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    grades = soup.find_all("div", {"class": "grade"})
    first_name = soup.findall("span", {"class": "pfname"})[0].text.strip()
    last_name = soup.findall("span", {"class": "plname"})[0].text.strip()
    department = soup.findall("div", {"class": "result-title"})[0].text.strip()
    professor_info = {
        'first_name': first_name,
        'last_name': last_name,
        'department': department.split('department')[0].split('fessor in the')[1].strip(),
        'overall_quality': grades[0].text.strip(),
        'would_take_again': grades[1].text.strip(),
        'level_of_difficulty': grades[2].text.strip()
    }
    return professor_info


# holder
