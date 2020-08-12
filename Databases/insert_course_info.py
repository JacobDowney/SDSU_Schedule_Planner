import sqlite3

# NOTE: this is not handled by users so its safe from SQL Injection

# Course_infos is not a CourseInfo object its a tuple of all the information
def InsertCourseInfos(course_period, course_infos):
    # Database file
    db_file = f"./Databases/{course_period}.db"

    # Create sql cursor to course period database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Every course info is unique so no need to check
    main_infos = [x[:-2] for x in course_infos]
    cursor.executemany(f"""
        INSERT INTO
            {course_period}_main
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, main_infos)
    main_id = cursor.lastrowid

    # For each course info insert it into database
    for course_info in course_infos:

        # Inserting footnotes into footnote and main_to_footnote tables
        footnotes = course_info[-1]
        footnote_ids = []
        for footnote in footnotes:
            footnote_id = get_id_or_insert(
                cursor,
                f"{course_period}_footnote",
                f"CODE = '{footnote}'",
                f"('{footnote[0]}', '{footnote[1]}')"
            )
            footnote_ids.append(footnote_id)
        main_to_footnote = [[main_id, x] for x in footnote_ids]
        insert_main_to_id(
            cursor, f"{course_period}_main_id_to_footnote_id", main_to_footnote
        )

        # Inserting meetings into meeting and main_to_meeting tables
        meetings = course_info[-2]
        meeting_ids = []
        for meeting in meetings:
            meeting_id = get_id_or_insert(
                cursor,
                f"{course_period}_meeting",
                f"""
                        TITLE = '{course_info[2]}'
                    AND
                        TYPE = '{meeting[0]}'
                    AND
                        TIMESTART = '{meeting[1]}'
                    AND
                        TIMEEND = '{meeting[2]}'
                    AND
                        DAY = '{meeting[3]}'
                    AND
                        LOCATION = '{meeting[4]}
                """,
                f"""
                    ('{course_info[2]}', '{meeting[0]}', '{meeting[1]}',
                     '{meeting[2]}', '{meeting[3]}', '{meeting[4]}')
                """
            )
            meeting_ids.append(meeting_id)

            # Inserting instructors into instructor and meeting_to_instructor
            # tables
            instructors = meeting[5]
            instructor_ids = []
            for instructor in instructors:
                instructor_id = get_id_or_insert(
                    cursor,
                    f"{course_period}_instructor",
                    f"""
                            FIRSTNAME = '{instructor[0]}'
                        AND
                            LASTNAME = '{instructor[1]}'
                        AND
                            DEPARTMENT = '{instructor[2]}'
                    """,
                    f"""
                        ('{instructor[0]}', '{instructor[1]}',
                         '{instructor[2]}', '{instructor[3]}',
                         '{instructor[4]}', '{instructor[4]}')
                    """
                )
                instructor_ids.append(instructor_id)
            meeting_to_instructor = [[meeting_id, x] for x in instructor_ids]
            insert_main_to_id(
                cursor,
                f"{course_period}_meeting_id_to_instructor_id",
                meeting_to_instructor
            )

        main_to_meeting = [[main_id, x] for x in meeting_ids]
        insert_main_to_id(
            cursor, f"{course_period}_main_id_to_meeting_id", main_to_meeting
        )

    # Commit all changes to database
    conn.commit()
    # Close our connection
    conn.close()

def get_id_or_insert(cursor, table, where, values):
    cursor.execute(f"""
        SELECT
            rowid
        FROM
            {table}
        WHERE
            {where}
    """)
    id = cursor.fetchone()
    if id != None:
        return id
    cursor.execute(f"""
        INSERT INTO
            {table}
        VALUES
            {values}
    """)
    return cursor.lastrowid

def insert_main_to_id(cursor, table, values):
    cursor.execute(f"""
        INSERT INTO
            {table}
        VALUES
            (?, ?)
    """, values)
