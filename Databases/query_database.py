import sqlite3

def QueryCourseInfo(course_period, course_subject, course_num):
    # Database file
    db_file = f"./Databases/{course_period}.db"

    # SQL Create Table Instruction
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Query for course info
    cursor.execute("""
        SELECT
            rowid, *
        FROM
            %(period)s
        WHERE
            SUBJECT = %(subject)s
        AND
            NUMBER = %(num)s
    """, {
            'period': course_period + "_main",
            'subject': course_subject,
            'num': course_num,
        }
    )
    main_results = cursor.fetchall()

    course_infos = []
    for main_result in main_results:
        main_row_id = main_result[0]

        footnotes = []
        footnote_ids = select_helper(cursor, "FOOTNOTEROWID", period+"_main_id_to_footnote_id", "MAINROWID", main_row_id)
        for footnote_id in footnote_ids:
            footnote_info = select_helper(cursor, "row_id, *", period+"_footnote", "rowid", footnote_id)
            footnotes.append(footnote.Footnote(footnote_info))

        meetings = []
        meeting_ids = select_helper(cursor, "MEETINGROWID", period+"_main_id_to_meeting_id", "MAINROWID", main_row_id)
        for meeting_id in meeting_ids:
            meeting_info = select_helper(cursor, "rowid, *", period+"_meeting", "rowid", meeting_id)
            instructors = []
            instructor_ids = select_helper(cursor, "INSTRUCTORROWID", period+"_meeting_id_to_instructor_id", "MEETINGROWID", meeting_id)
            for instructor_id in instructor_ids:
                instructor_info = select_helper(cursor, "rowid, *", period+"_instructor", "rowid", instructor_id)
                instructors.append(instructor.Instructor(instructor_info))
            meetings.append(meeting.Meeting(meeting_info, instructors))

        course_infos.append(
            course_info.CourseInfo(main_result, meetings, footnotes)
        )

    # Commit all changes to database
    conn.commit()
    # Close our connection
    conn.close()

    return course_infos


def select_helper(cursor, ids, table_name, row_id_1, row_id_2):
    cursor.execute("""
        SELECT
            %(select)s
        FROM
            %(from)s
        WHERE
            %(comp_1)s = %(comp_2)s
    """, {
            'select': ids,
            'from': table_name,
            'comp_1': row_id_1,
            'comp_2': row_id_2,
        }
    )
    return cursor.fetchall()
