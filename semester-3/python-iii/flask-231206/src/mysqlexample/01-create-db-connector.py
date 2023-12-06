import os
from mysql.connector import connection

# Connect to MySQL server
with connection.MySQLConnection(user='root', password=os.environ["MYSQL_PASSWORD"],
                                 host='localhost') as cnx:
    cursor = cnx.cursor()

    # Get the version of the MySQL server
    cursor.execute("SELECT VERSION()")
    result = cursor.fetchone()
    print(result)

    # Create a database if not exist.
    cursor.execute("CREATE DATABASE IF NOT EXISTS example_c DEFAULT CHARSET utf8 COLLATE utf8_general_ci")

    cnx.commit()
