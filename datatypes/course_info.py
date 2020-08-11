class CourseInfo:
    def __init__(self, rowid, subject, number, title, section, sched_num, units,
                 session, seats_open, full_title, description, prerequisite,
                 statement, meetings, footnotes):
        self.rowid = rowid
        self.subject = subject
        self.number = number
        self.title = title
        self.section = section
        self.sched_num = sched_num
        self.units = units
        self.session = session
        self.seats_open = seats_open
        self.full_title = full_title
        self.description = description
        self.prerequisite = prerequisite
        self.statement = statement
        self.meetings = meetings
        self.footnotes = footnotes


    def __init__(self, course_info_list, meetings, footnotes):
        self.rowid = course_info_list[0]
        self.subject = course_info_list[1]
        self.number = course_info_list[2]
        self.title = course_info_list[3]
        self.section = course_info_list[4]
        self.sched_num = course_info_list[5]
        self.units = course_info_list[6]
        self.session = course_info_list[7]
        self.seats_open = course_info_list[8]
        self.full_title = course_info_list[9]
        self.description = course_info_list[10]
        self.prerequisite = course_info_list[11]
        self.statement = course_info_list[12]
        self.meetings = meetings
        self.footnotes = footnotes

    def get_rowid(self):
        return self.rowid

    def get_subject(self):
        return self.subject

    def get_number(self):
        return self.number

    def get_title(self):
        return self.title

    def get_section(self):
        return self.section

    def get_sched_num(self):
        return self.sched_num

    def get_units(self):
        return self.units

    def get_session(self):
        return self.session

    def get_seats_open(self):
        return self.seats_open

    def get_full_title(self):
        return self.full_title

    def get_description(self):
        return self.description

    def get_prerequisite(self):
        return self.prerequisite

    def get_statement(self):
        return self.statement

    def get_meetings(self):
        return self.meetings

    def get_footnotes(self):
        return self.footnotes
