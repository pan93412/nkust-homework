import os
from sqlalchemy import Column, MetaData, String, Table, create_engine, insert, select

# Create a connection to the database
engine = create_engine(f'mysql+mysqlconnector://root:{os.environ["MYSQL_PASSWORD"]}@localhost/example_sa')

# Create a metadata with the tables.
metadata = MetaData()

# Create a stu_data table, with:
#     stu_no as primary key
#     stu_name
#     stu_class
#     stu_phone
Student = Table(
    "students",
    metadata,
    Column("stu_no", String(10), primary_key=True),
    Column("stu_name", String(255), nullable=False),
    Column("stu_class", String(255), nullable=False),
    Column("stu_phone", String(10), nullable=False),
)

with engine.connect() as connection:
    # Create a table if not exist.
    metadata.create_all(engine)

    # Insert data into stu_data table
    stmt = insert(Student).values([
        {"stu_no": "C111156101", "stu_name": "王小明", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156102", "stu_name": "陳小華", "stu_class": "智商二甲", "stu_phone": "0913579246"},
        {"stu_no": "C111156103", "stu_name": "林小美", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156104", "stu_name": "張小強", "stu_class": "智商二甲", "stu_phone": "0913579246"},
        {"stu_no": "C111156105", "stu_name": "李大雄", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156106", "stu_name": "黃小琪", "stu_class": "智商二甲", "stu_phone": "0913579246"},
        {"stu_no": "C111156107", "stu_name": "吳小菁", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156108", "stu_name": "劉小偉", "stu_class": "智商二甲", "stu_phone": "0913579246"},
        {"stu_no": "C111156109", "stu_name": "蔡小娟", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156110", "stu_name": "許小儒", "stu_class": "智商二甲", "stu_phone": "0913579246"},
        {"stu_no": "C111156111", "stu_name": "林小雨", "stu_class": "智商二甲", "stu_phone": "0912345678"},
        {"stu_no": "C111156112", "stu_name": "陳小風", "stu_class": "智商二甲", "stu_phone": "0913579246"},
    ])
    result = connection.execute(stmt)
    print("Inserted %d rows" % result.rowcount)
    connection.commit()

    # Get all datas from stu_data table
    stmt = select(Student)
    result = connection.execute(stmt)
    print(result.fetchall())

