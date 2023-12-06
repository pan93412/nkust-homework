import os
from mysql.connector import connection
# Connect to MySQL server
with connection.MySQLConnection(user='root', password=os.environ["MYSQL_PASSWORD"],
                                 host='localhost', database='example_c') as cnx:
    cursor = cnx.cursor()

    # Insert data into stu_data table
    cursor.executemany(
        "INSERT INTO stu_data (stu_no, stu_name, stu_class, stu_phone) VALUES (%s, %s, %s, %s)",
        [
            # 15 mock data
            ("C111156101", "王小明", "智商二甲", "0912345678"),
            ("C111156102", "陳小華", "智商二甲", "0913579246"),
            ("C111156103", "林小美", "智商二甲", "0912345678"),
            ("C111156104", "張小強", "智商二甲", "0913579246"),
            ("C111156105", "李大雄", "智商二甲", "0912345678"),
            ("C111156106", "黃小琪", "智商二甲", "0913579246"),
            ("C111156107", "吳小菁", "智商二甲", "0912345678"),
            ("C111156108", "劉小偉", "智商二甲", "0913579246"),
            ("C111156109", "蔡小娟", "智商二甲", "0912345678"),
            ("C111156110", "許小儒", "智商二甲", "0913579246"),
            ("C111156111", "林小雨", "智商二甲", "0912345678"),
            ("C111156112", "陳小風", "智商二甲", "0913579246"),
            ("C111156113", "黃小雲", "智商二甲", "0912345678"),
            ("C111156114", "張小翰", "智商二甲", "0913579246"),
            ("C111156115", "王小明", "智商二甲", "0912345678"),
        ]
    )
    cnx.commit()

    # Get all datas from stu_data table
    cursor.execute("SELECT * FROM stu_data")
    result = cursor.fetchall()
    print(result)
