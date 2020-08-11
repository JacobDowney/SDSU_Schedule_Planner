import sqlite3

def query_course_info(course_period, course_subject, course_num):
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
        course_info = {
            'row_id': main_row_id,
            'subject': main_result[1],
            'number': main_result[2],
            'title': main_result[3],
            'section': main_result[4],
            'sched_num': main_result[5],
            'units': main_result[6],
            'session': main_result[7],
            'seats_open': main_result[8],
            'full_title': main_result[9],
            'description': main_result[10],
            'prerequisite': main_result[11],
            'statement': main_result[12],
        }
        footnotes = []
        footnote_ids = select_helper(cursor, "FOOTNOTEROWID", period+"_main_id_to_footnote_id", "MAINROWID", main_row_id)
        for footnote_id in footnote_ids:
            footnote_info = select_helper(cursor, "row_id, *", period+"_footnote", "rowid", footnote_id)
            footnote = {
                'row_id': footnote_info[0],
                'code': footnote_info[1],
                'details': footnote_info[2],
            }
            footnotes.append(footnote)
        course_info['footnotes'] = footnotes

        meetings = []
        meeting_ids = select_helper(cursor, "MEETINGROWID", period+"_main_id_to_meeting_id", "MAINROWID", main_row_id)
        for meeting_id in meeting_ids:
            meeting_info = select_helper(cursor, "rowid, *", period+"_meeting", "rowid", meeting_id)
            meeting = {
                'row_id': meeting_info[0],
                'type': meeting_info[1],
                'time_start': meeting_info[2],
                'time_end': meeting_info[3],
                'day': meeting_info[4],
                'location': meeting_info[5],
            }
            instructors = []
            instructor_ids = select_helper(cursor, "INSTRUCTORROWID", period+"_meeting_id_to_instructor_id", "MEETINGROWID", meeting_id)
            for instructor_id in instructor_ids:
                instructor_info = select_helper(cursor, "rowid, *", period+"_instructor", "rowid", instructor_id)
                instructor = {
                    'row_id': instructor_info[0],
                    'first_name': instructor_info[1],
                    'last_name': instructor_info[2],
                    'department': instructor_info[3],
                    'overall': instructor_info[4],
                    'take_again': instructor_info[5],
                    'difficulty': instructor_info[6],
                }
                instructors.append(instructor)
            meeting['instructors'] = instructors
        course_info['meetings'] = meetings

        course_infos.append(course_info)

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
