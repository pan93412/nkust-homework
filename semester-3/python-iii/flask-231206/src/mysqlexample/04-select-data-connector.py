import os
from mysql.connector import connection
# Connect to MySQL server
with connection.MySQLConnection(user='root', password=os.environ["MYSQL_PASSWORD"],
                                 host='localhost', database='example_c') as cnx:
    cursor = cnx.cursor()

    # 輸入一個學號，查詢該學生的資料
    stu_no = input("請輸入學號: ")

    # 從資料庫查詢特定資料
    cursor.execute("SELECT * FROM stu_data WHERE stu_no = %s", (stu_no,))

    result = cursor.fetchone()
    print(result)
