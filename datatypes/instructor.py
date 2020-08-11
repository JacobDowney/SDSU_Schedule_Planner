class Instructor:
    def __init__(self, rowid, first_name, last_name, department, overall, take_again, difficulty):
        self.rowid = rowid
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.overall = overall
        self.take_again = take_again
        self.difficulty = difficulty

    def __init__(self, instructor_info_list):
        self.rowid = instructor_info_list[0]
        self.first_name = instructor_info_list[1]
        self.last_name = instructor_info_list[2]
        self.department = instructor_info_list[3]
        self.overall = instructor_info_list[4]
        self.take_again = instructor_info_list[5]
        self.difficulty = instructor_info_list[6]

    def get_rowid(self):
        return self.rowid

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_department(self):
        return self.department

    def get_overall(self):
        return self.overall

    def get_take_again(self):
        return self.take_again

    def get_difficulty(self):
        return self.difficulty
