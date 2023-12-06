import os
from mysql.connector import connection
# Connect to MySQL server
with connection.MySQLConnection(user='root', password=os.environ["MYSQL_PASSWORD"],
                                 host='localhost', database='example_c') as cnx:

    cursor = cnx.cursor()

    # Create a stu_data table, with:
    #     stu_no as primary key
    #     stu_name
    #     stu_class
    #     stu_phone

    # Create a table if not exist.
    cursor.execute((
        "CREATE TABLE IF NOT EXISTS stu_data ("
        "stu_no VARCHAR(10) PRIMARY KEY,"
        "stu_name VARCHAR(255) NOT NULL,"
        "stu_class VARCHAR(255) NOT NULL,"
        "stu_phone VARCHAR(10) NOT NULL)"
    ))

    cnx.commit()
