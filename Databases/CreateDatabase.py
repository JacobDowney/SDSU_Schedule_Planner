import sqlite3

create_main = """CREATE TABLE IF NOT EXISTS main(
                        MAINID INTEGER PRIMARY KEY,
                        SUBJECT ENUM('A+E',   'A+S',   'ACCTG', 'AFRAS', 'AMIND',
                                     'ANTH',  'ARAB',  'ARP',   'ART',   'ASIAN',
                                     'ASTR',  'AUD',   'B+A',   'BIOL',  'BIOMI',
                                     'C+LT',  'C+P',   'CAL',   'CCS',   'CFD',
                                     'CHEM',  'CHIN',  'CINTS', 'CIV+E', 'CJ',
                                     'CLASS', 'COMM',  'COMP',  'COMPE', 'CON+E',
                                     'CS',    'CSP',   'DANCE', 'DLE',   'DPT',
                                     'E+E',   'ECON',  'ED',    'EDL',   'ENGL',
                                     'ENGR',  'ENS',   'ENV+E', 'ENV+S', 'EUROP',
                                     'FILIP', 'FIN',   'FRENC', 'GEN+S', 'GEOG',
                                     'GEOL',  'GERMN', 'GERO',  'GMS',   'H+SEC',
                                     'HEBRW', 'HHS',   'HIST',  'HONOR', 'HTM',
                                     'HUM',   'I+B',   'INT+S', 'ISCOR', 'ITAL',
                                     'JAPAN', 'JMS',   'JS',    'KOR',   'LATAM',
                                     'LDT',   'LGBT',  'LIB+S', 'LING',  'M+BIO',
                                     'M+E',   'M+S+E', 'MALAS', 'MATH',  'MGT',
                                     'MIL+S', 'MIS',   'MKTG',  'MTHED', 'MUSIC',
                                     'N+SCI', 'NAV+S', 'NURS',  'NUTR',  'OCEAN',
                                     'P+A',   'P+H',   'PERS',  'PHIL',  'PHYS',
                                     'POL+S', 'PORT',  'PSFA',  'PSY',   'R+A',
                                     'REL+S', 'RTM',   'RUSSN', 'RWS',   'SCI',
                                     'SLHS',  'SOC',   'SPAN',  'SPED',  'STAT',
                                     'SUSTN', 'SWORK', 'TE',    'TFM',   'THEA',
                                     'WMNST'),
                        NUMBER TEXT,
                        TITLE TEXT,
                        SECTION TEXT,
                        SCHEDNUM TEXT,
                        UNITS TEXT,
                        SESSION TEXT,
                        SEATSOPEN TEXT,
                        FULLTITLE TEXT,
                        DESCRIPTION TEXT,
                        PREREQUISITE TEXT,
                        STATEMENT TEXT)"""

create_main_id_to_meeting_id = """CREATE TABLE IF NOT EXISTS main_id_to_meeting_id(
                        MAINID INTEGER,
                        MEETINGID INTEGER)"""

create_main_id_to_footnote_id = """CREATE TABLE IF NOT EXISTS main_id_to_footnote_id(
                        MAINID INTEGER,
                        FOOTNOTEID INTEGER)"""

create_meeting_id_to_instructor_id = """CREATE TABLE IF NOT EXISTS meeting_id_to_instructor_id(
                        MEETINGID INTEGER,
                        INSTRUCTORID INTEGER)"""

create_meeting = """CREATE TABLE IF NOT EXISTS meeting(
                        MEETINGID INTEGER PRIMARY KEY,
                        TYPE TEXT,
                        TIMESTART TIME,
                        TIMEEND TIME,
                        DAY TEXT,
                        LOCATION TEXT)"""

create_footnote = """CREATE TABLE IF NOT EXISTS footnote(
                        FOOTNOTEID INTEGER PRIMARY KEY,
                        CODE TEXT,
                        DETAILS TEXT)"""

create_instructor = """CREATE TABLE IF NOT EXISTS instructor(
                        INSTRUCTORID INTEGER PRIMARY KEY,
                        FIRSTNAME TEXT,
                        LASTNAME TEXT,
                        DEPARTMENT TEXT,
                        OVERALL INTEGER,
                        TAKEAGAIN INTEGER,
                        DIFFICULTY INTEGER)"""


# Creates a connection with the db_file file
def create_connection(db_file):
    connection = sqlite3.connect(db_file)
    return connection


# Runs the command to create the table
def create_table(connection, create_sql_table_command):
    cursor = connection.cursor()
    cursor.execute(create_sql_table_command)


# ENUMS FOR DAY???
# Multiple class per sched num -> comm 101
def main():
    # Database file
    database = "./spring2019.db"
    # SQL Create Table Instruction

    create_table(create_sql_table)


if __name__ == '__main__':
    main()
else:
    print "Not Supported"
