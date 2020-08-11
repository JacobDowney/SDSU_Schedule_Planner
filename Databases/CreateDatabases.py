import sqlite3

#cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});

#period = "p_20204"  # this is fall 2020

# Could be part of a block of sections
def create_main(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_main (
            SUBJECT TEXT,
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
            STATEMENT TEXT
        )"""

def create_meeting(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_meeting(
            TYPE TEXT,
            TIMESTART TEXT,
            TIMEEND TEXT,
            DAY TEXT,
            LOCATION TEXT
        )"""

def create_instructor(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_instructor(
            FIRSTNAME TEXT,
            LASTNAME TEXT,
            DEPARTMENT TEXT,
            OVERALL INTEGER,
            TAKEAGAIN INTEGER,
            DIFFICULTY INTEGER
        )"""

def create_footnote(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_footnote(
            CODE TEXT,
            DETAILS TEXT
        )"""

def create_main_id_to_meeting_id(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_main_id_to_meeting_id(
            MAINROWID INTEGER,
            MEETINGROWID INTEGER
        )"""

def create_main_id_to_footnote_id(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_main_id_to_footnote_id(
            MAINROWID INTEGER,
            FOOTNOTEROWID INTEGER
        )"""

def create_meeting_id_to_instructor_id(period):
    return f"""
        CREATE TABLE IF NOT EXISTS {period}_meeting_id_to_instructor_id(
            MEETINGROWID INTEGER,
            INSTRUCTORROWID INTEGER
        )"""

# Runs the command to create the table
def create_table(connection, create_sql_table_command):
    cursor = connection.cursor()
    cursor.execute(create_sql_table_command)


# Multiple class per sched num -> comm 101
def main():
    period = "p_20204"

    # Database file
    db_file = f"./Databases/{period}.db"

    # SQL Create Table Instruction
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create all necesary tables
    cursor.execute(create_main(period))
    cursor.execute(create_meeting(period))
    cursor.execute(create_instructor(period))
    cursor.execute(create_footnote(period))
    cursor.execute(create_main_id_to_meeting_id(period))
    cursor.execute(create_main_id_to_footnote_id(period))
    cursor.execute(create_meeting_id_to_instructor_id(period))

    # Commit all changes to database
    conn.commit()

    # Close our connection
    conn.close()


if __name__ == '__main__':
    main()
else:
    print("Not Supported")
