import sqlite3
import SchedulePlanner

# Creates a connection with the db_file file
def create_connection(db_file):
    connection = sqlite3.connect(db_file)
    return connection

# Runs the command to create the table
def add_to_table(connection, add_to_sql_table_command):
    cursor = connection.cursor()
    cursor.execute(add_to_sql_table_command)
    connection.commit()

# ENUMS FOR DAY???
# Multiple class per sched num -> comm 101
def main():
    # Database file
    database = "./spring2019.db"

    courses = SchedulePlanner.get_dict_of_all_courses()

    for course in courses:
        add_to_sql_table = """INSERT""".format()



if __name__ == '__main__':
    main()
else:
    print "Not Supported"
