import os
from sqlalchemy import Column, MetaData, String, Table, create_engine, insert, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Create a connection to the database
engine = create_engine(f'mysql+mysqlconnector://root:{os.environ["MYSQL_PASSWORD"]}@localhost/example_sa')


class Base(DeclarativeBase): pass

class Student(Base):
    __tablename__ = "students"

    stu_no: Mapped[str] = mapped_column(String(10), primary_key=True)
    stu_name: Mapped[str] = mapped_column(String(255), nullable=False)
    stu_class: Mapped[str] = mapped_column(String(255), nullable=False)
    stu_phone: Mapped[str] = mapped_column(String(10), nullable=False)

    def __repr__(self):
        return f"<Student(stu_no='{self.stu_no}', stu_name='{self.stu_name}', stu_class='{self.stu_class}', stu_phone='{self.stu_phone}')>"

with Session(engine) as session:
    # Ask user to input a student number
    stu_no = input("請輸入學號: ")

    student = session.get(Student, stu_no)

    print(student if student else "Not found.")
