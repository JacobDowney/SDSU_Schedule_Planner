def print_prof(professor):
    print_str = ""
    print_str += professor['first_name']
    print_str += " "
    print_str += professor['last_name']
    print_str += ": "
    print_str += professor['overall_quality']
    return print_str

def get_course_str(course_dict, professor_dict):
    print_str = ""
    print_str += course_dict['name']
    print_str += "-"
    print_str += course_dict['number']
    print_str += ": "
    print_str += course_dict['sched']
    print_str += " = "
    print_str += course_dict['title']
    print_str += "\n"
    print_str += professor_dict['first_name']
    print_str += " "
    print_str += professor_dict['last_name']
    return print_str

def get_rate_my_prof_info(professor_info):
    print_str = (professor_info['first_name'] + ' '
                + professor_info['last_name'] + ' : '
                + professor_info['department'] + ' = '
                + professor_info['overall_quality'])
    return print_str
