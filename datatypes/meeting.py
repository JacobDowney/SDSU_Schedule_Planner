class Meeting:
    def __init__(self, rowid, type, time_start, time_end, day, location, instructors):
        self.rowid = rowid
        self.type = type
        self.time_start = time_start
        self.time_end = time_end
        self.day = day
        self.location = location
        self.instructors = instructors

    def __init__(self, meeting_info_list, instructors):
        self.rowid = meeting_info_list[0]
        self.type = meeting_info_list[1]
        self.time_start = meeting_info_list[2]
        self.time_end = meeting_info_list[3]
        self.day = meeting_info_list[4]
        self.location = meeting_info_list[5]
        self.instructors = instructors

    def get_rowid(self):
        return self.rowid

    def get_type(self):
        return self.type

    def get_time_start(self):
        return self.time_start

    def get_time_end(self):
        return self.time_end

    def get_day(self):
        return self.day

    def get_location(self):
        return self.location

    def get_instructors(self):
        return self.instructors
