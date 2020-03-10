from degree_evaluation import UserInformation
import degree_evaluation_formatter as formatter
import degree
import re

def main():
    #parse_degree_evaluation(degree.jd_degree)
    test_parse(degree.jd_degree)
    #parse_degree_evaluation_2(degree.jd_degree)

def test_parse(degree_evaluation):
    degree = degree_evaluation.split("Close All Sections -->")[1]
    sections = degree.split("Requirement:")
    count = -1
    for section in sections:
        count += 1
        if count == 0:
            continue
        pieces = section.split("Requirement expanded, click to collapseRequirement")
        print pieces[0].strip()
        info = pieces[1].strip()
        print info
        print "\n-----------------------\n"

def parse_degree_evaluation_2(degree_evaluation):
    run_pre_checks(degree_evaluation)

    info = degree_evaluation.split("*** DEGREE EVALUATION ***")

    if len(info) != 2:
        error("degree evaluation split should be 2 but is: " + str(len(info)))
    top_info = info[0].strip()
    info = info[1]

    user_information = UserInformation(get_user_information(top_info))

    pattern = "Requirement\:[a-zA-Z\s]*[\t\s]*Requirement\sexpanded,\sclick\sto\scollapseRequirement\s[a-zA-Z]*"
    regex = re.compile(pattern)
    all_found = regex.findall(info)
    for find in all_found:
        print find
    #return {'span': match.span(), 'text': match.group(0)}



def parse_degree_evaluation(degree_evaluation):
    run_pre_checks(degree_evaluation)

    info = degree_evaluation.split("*** DEGREE EVALUATION ***")

    if len(info) != 2:
        error("degree evaluation split should be 2 but is: " + str(len(info)))
    top_info = info[0].strip()
    info = info[1]

    user_information = UserInformation(get_user_information(top_info))


    competency_requirements = get_requirment_info(info, "\*{3}\sCOMPETENCY\sREQUIREMENTS\s\*{3}")
    graduation_writing_assessment_requirement = get_requirment_info(info, "\*{3}\sGRADUATION\sWRITING\sASSESSMENT\sREQUIREMENT\s\*{3}")
    american_institutions_requirements = get_requirment_info(info, "\*{3}\sAMERICAN\sINSTITUTIONS\sREQUIREMENT\s\*{3}")
    unit_residence_and_gpa_requirements = get_requirment_info(info, "\*{3}\sUNIT,\sRESIDENCE\sAND\sGPA\sREQUIREMENTS\s\*{3}")
    general_education_requirements = get_requirment_info(info, "\*{3}\sGENERAL\sEDUCATION\sREQUIREMENTS\s\*{3}")
    general_education_unit_requirements = get_requirment_info(info, "\*{3}\sGENERAL\sEDUCATION\sUNIT\sREQUIREMENTS\s\*{3}")
    communication_and_critical_thinking = get_requirment_info(info, "\*{3}\sI\.\sCOMMUNICATION\sAND\sCRITICAL\sTHINKING\s\*{3}")
    foundations_natural_sciences_and_quantitative_reasoning = get_requirment_info(info, "\*{3}\sIIA\.\sFOUNDATIONS\s\*{3}")
    foundations_social_and_behavioral_sciences = get_requirment_info(info, "\*{3}\sIIB\.\sFOUNDATIONS\s\-\sSOCIAL\sAND\sBEHAVIORAL\sSCIENCES\s\*{3}")
    foundations_humanities = get_requirment_info(info, "\*{3}\sIIC\.\sFOUNDATIONS\s\-\sHUMANITIES\s\*{3}")
    general_education_american_institutions = get_requirment_info(info, "\*{3}\sIII\.\sGENERAL\sEDUCATION\sAMERICAN\sINSTITUTIONS\s\*{3}")
    explorations = get_requirment_info(info, "\*{3}\sIV\.\sEXPLORATIONS\s\*{3}")
    cultural_diversity = get_requirment_info(info, "\*{3}\sCULTURAL\sDIVERSITY\s\*{3}")
    explorations_natural_sciences = get_requirment_info(info, "\*{3}\sIVA\.\sEXPLORATIONS\s\-\sNATURAL\sSCIENCES\s\*{3}")
    explorations_social_and_behavioral_sciences = get_requirment_info(info, "\*{3}\sIVB\.\sEXPLORATIONS\s\-\sSOCIAL\sAND\sBEHAVIORAL\sSCIENCES\s\*{3}")
    explorations_humanities = get_requirment_info(info, "\*{3}\sIVC\.\sEXPLORATIONS\s\-\sHUMANITIES\s\*{3}")
    major_requirements_catalog_year = get_requirment_info(info, "\*{3}\sMAJOR\sREQUIREMENTS\s\*{3}\nCatalog\sYear")
    preparation_for_the_major = get_requirment_info(info, "\*{3}\sPREPARATION\sFOR\sTHE\sMAJOR\s\*{3}")
    major_requirements = info.split("*** MAJOR REQUIREMENTS ***")[2].split("***")[0].strip()
    academic_coursework = get_requirment_info(info, "\*{4}\sACADEMIC\sCOURSEWORK\s\*{4}")

    text = competency_requirements['text']
    start = competency_requirements['span'][1]
    end = graduation_writing_assessment_requirement['span'][0]
    competency_requirements_formatted = formatter.format_competency_requirments(text, info[start:end])

    print "\n"
    text = graduation_writing_assessment_requirement['text']
    start = graduation_writing_assessment_requirement['span'][1]
    end = american_institutions_requirements['span'][0]
    graduation_writing_assessment_requirement_formatted = formatter.format_graduation_writing_assessment_requirement(text, info[start:end])
"""
    text = american_institutions_requirements['text']
    start = american_institutions_requirements['span'][1]
    end = graduation_writing_assessment_requirement['span'][0]
    american_institutions_requirements_formatted = formatter.format_american_institutions_requirements(text, info[start:end])

    text = unit_residence_and_gpa_requirements['text']
    start = unit_residence_and_gpa_requirements['span'][1]
    end = american_institutions_requirements['span'][0]
    unit_residence_and_gpa_requirements_formatted = formatter.format_(text, info[start:end])

    text = general_education_requirements['text']
    start = general_education_requirements['span'][1]
    end = unit_residence_and_gpa_requirements['span'][0]
    general_education_requirements_formatted = formatter.format_(text, info[start:end])

    text = general_education_unit_requirements['text']
    start = general_education_unit_requirements['span'][1]
    end = general_education_requirements['span'][0]
    general_education_unit_requirements_formatted = formatter.format_(text, info[start:end])

    text = communication_and_critical_thinking['text']
    start = communication_and_critical_thinking['span'][1]
    end = general_education_unit_requirements['span'][0]
    communication_and_critical_thinking_formatted = formatter.format_(text, info[start:end])

    text = foundations_natural_sciences_and_quantitative_reasoning['text']
    start = foundations_natural_sciences_and_quantitative_reasoning['span'][1]
    end = communication_and_critical_thinking['span'][0]
    foundations_natural_sciences_and_quantitative_reasoning_formatted = formatter.format_(text, info[start:end])

    text = foundations_social_and_behavioral_sciences['text']
    start = foundations_social_and_behavioral_sciences['span'][1]
    end = foundations_natural_sciences_and_quantitative_reasoning['span'][0]
    foundations_social_and_behavioral_sciences_formatted = formatter.format_(text, info[start:end])

    text = foundations_humanities['text']
    start = foundations_humanities['span'][1]
    end = foundations_social_and_behavioral_sciences['span'][0]
    foundations_humanities_formatted = formatter.format_(text, info[start:end])

    text = general_education_american_institutions['text']
    start = general_education_american_institutions['span'][1]
    end = foundations_humanities['span'][0]
    general_education_american_institutions_formatted = formatter.format_(text, info[start:end])

    text = explorations['text']
    start = explorations['span'][1]
    end = general_education_american_institutions['span'][0]
    explorations_formatted = formatter.format_(text, info[start:end])

    text = cultural_diversity['text']
    start = cultural_diversity['span'][1]
    end = explorations['span'][0]
    cultural_diversity_formatted = formatter.format_(text, info[start:end])

    text = explorations_natural_sciences['text']
    start = explorations_natural_sciences['span'][1]
    end = cultural_diversity['span'][0]
    explorations_natural_sciences_formatted = formatter.format_(text, info[start:end])

    text = explorations_social_and_behavioral_sciences['text']
    start = explorations_social_and_behavioral_sciences['span'][1]
    end = explorations_natural_sciences['span'][0]
    explorations_social_and_behavioral_sciences_formatted = formatter.format_(text, info[start:end])

    text = explorations_humanities['text']
    start = explorations_humanities['span'][1]
    end = explorations_social_and_behavioral_sciences['span'][0]
    explorations_humanities_formatted = formatter.format_(text, info[start:end])

    text = major_requirements_catalog_year['text']
    start = major_requirements_catalog_year['span'][1]
    end = explorations_humanities['span'][0]
    major_requirements_catalog_year_formatted = formatter.format_(text, info[start:end])

    text = preparation_for_the_major['text']
    start = preparation_for_the_major['span'][1]
    end = major_requirements_catalog_year['span'][0]
    preparation_for_the_major_formatted = formatter.format_(text, info[start:end])

    text = major_requirements['text']
    start = major_requirements['span'][1]
    end = preparation_for_the_major['span'][0]
    major_requirements_formatted = formatter.format_(text, info[start:end])

    text = academic_coursework['text']
    start = academic_coursework['span'][1]
    end = major_requirements['span'][0]
    academic_coursework_formatted = formatter.format_(text, info[start:end])

    degree_infos_formatted =
        [competency_requirements_formatted,
        graduation_writing_assessment_requirement_formatted,
        american_institutions_requirements_formatted,
        unit_residence_and_gpa_requirements_formatted,
        general_education_requirements_formatted,
        general_education_unit_requirements_formatted,
        communication_and_critical_thinking_formatted,
        foundations_natural_sciences_and_quantitative_reasoning_formatted,
        foundations_social_and_behavioral_sciences_formatted,
        foundations_humanities_formatted,
        general_education_american_institutions_formatted,
        explorations_formatted,
        cultural_diversity_formatted,
        explorations_natural_sciences_formatted,
        explorations_social_and_behavioral_sciences_formatted,
        explorations_humanities_formatted,
        major_requirements_catalog_year_formatted,
        preparation_for_the_major_formatted,
        major_requirements_formatted,
        academic_coursework_formatted]

    for degree_info_formatted in degree_infos_formatted:

    index = 0
    for degree_info in degree_infos:
        start_info = degree_infos[index]['span'][1]
        end_info = degree_infos[index + 1]['span'][0]
        print "%d\n%s\n%s\n" % (index + 1, str(degree_info), info[start_info:end_info])
        index += 1
    """

    #coursework_totals = CourseworkTotals(get_coursework_totals(academic_coursework))


# Takes in a top info and strips the important info and returns it as a dict.
def get_user_information(top_info):
    top_info = top_info.split("\n")
    if len(top_info) != 9:
        error("WRONG USER INFO LENGTH")
    user_information = {
        'name': top_info[0].strip(),
        'major': top_info[1].strip(),
        'prepared_on': top_info[2].strip().split("Prepared On")[1].strip().split("Program Code")[0].strip(),
        'program_code': top_info[2].strip().split("Program Code")[1].strip().split("Catalog Year")[0].strip(),
        'catalog_year': top_info[2].strip().split("Catalog Year")[1].strip(),
        'student_id': top_info[3].strip().split("Student ID")[1].split("Graduation Date")[0].strip(),
        'graduation_date': top_info[3].strip().split("Graduation Date")[1].strip(),
        'all_requirements_complete': "AT LEAST ONE REQUIREMENT HAS NOT BEEN SATISFIED" not in top_info[7]
    }
    return user_information

def get_coursework_totals(academic_coursework):
    cumulative = academic_coursework.split("Sub-Requirement	SDSU CUMULATIVE TOTALS")[1]

    """
    Sub-Requirement	SDSU CUMULATIVE TOTALS
( 62.0UNITS EARNED)		  Sub-Requirement
62.0UNITS ATTEMPTED 226.4	POINTS 3.651	GPA   Sub-Requirement	TRANSFER CUMULATIVE TOTALS
( 19.0UNITS EARNED)		  Sub-Requirement
0.0UNITS ATTEMPTED 0.0	POINTS	  Sub-Requirement	TOTAL UNITS EARNED
( 81.0UNITS EARNED)		  Sub-Requirement
62.0UNITS ATTEMPTED 226.4	POINTS 3.651	GPA
    """

# Takes in info and parses it for the first thing right after the requirement
def get_requirment_info(info, pattern):
    regex = re.compile(pattern)
    match = regex.search(info)
    return {'span': match.span(), 'text': match.group(0)}

def run_pre_checks(info):
    info = info.split("*** DEGREE EVALUATION ***")
    if len(info) != 2:
        error("pre-check: 1")
    top = info[0]
    bottom = info[1]
    info = info[1]

    info = info.split("*** MAJOR REQUIREMENTS ***\nCatalog Year")
    if len(info) != 2:
        error("pre-check: 2")
    main_part = info[0]
    grades = info[1]

    if len(main_part.split("***")) != 35:
        error("pre-check: 3 (main part)")






def error(error):
    print "ERROR: " + error

if __name__ == '__main__':
    main()
else:
    print "Not Supported"
