class Footnote:
    def __init__(self, rowid, code, details):
        self.rowid = rowid
        self.code = code
        self.details = details

    def __init__(self, footnote_info_list):
        self.rowid = footnote_info_list[0]
        self.code = footnote_info_list[1]
        self.details = footnote_info_list[2]

    def get_rowid(self):
        return self.rowid

    def get_code(self):
        return self.code

    def get_details(self):
        return self.details
