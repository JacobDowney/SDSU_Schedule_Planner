import sqlite3

# NOTE: this is not handled by users so its safe from SQL Injection

# Course_infos is not a CourseInfo object its a tuple of all the information
def InsertCourseInfos(course_period, course_infos):
    # Database file
    db_file = f"./Databases/{course_period}.db"

    # Create sql cursor to course period database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # ASSUMING EVERY COURSE_INFO IS UNIQUE

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

        # Inserting footnotes
        footnotes = course_info[-1]
        footnote_ids = []
        for footnote in footnotes:
            cursor.execute(f"""
                SELECT
                    rowid
                FROM
                    {course_period}_footnote
                WHERE
                    CODE = {footnote}
            """)
            code = cursor.fetchone()
            if code == None:
                cursor.execute(f"""
                    INSERT INTO
                        {course_period}_footnote
                    VALUES
                        ('{footnote[0]}', '{footnote[1]}')
                """)
                code = cursor.lastrowid
            footnote_ids.append(code)
        main_to_footnote = [[main_id, x] for x in footnote_ids]
        cursor.execute(f"""
            INSERT INTO
                {course_period}_main_id_to_footnote_id
            VALUES
                (?, ?)
        """, main_to_footnote)

        # Insert meeting
        meetings = course_info[-2]
        # We assume that the main has not yet been inserted
        # Insert main

        # CREATE TABLE bookmarks(
        #     users_id INTEGER,
        #     lessoninfo_id INTEGER,
        #     UNIQUE(users_id, lessoninfo_id)
        # );
        #
        # INSERT OR IGNORE INTO bookmarks(users_id, lessoninfo_id) VALUES(123, 456)

    # Commit all changes to database
    conn.commit()
    # Close our connection
    conn.close()

def InsertCourseInfo(course_period, course_info):
    # Database file
    db_file = f"./Databases/{course_period}.db"

    # Create sql cursor to course period database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Insert course info into database
    insert_course_info(cursor, course_period, course_info)

    # Commit all changes to database
    conn.commit()
    # Close our connection
    conn.close()

# Private below

def insert_course_info(cursor, course_period, course_info):

    return 5
