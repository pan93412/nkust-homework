import os
from sqlalchemy import String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import tkinter
import tkinter.messagebox
from tkinter.ttk import Button, Entry, Frame, Label


class Base(DeclarativeBase): pass

class Student(Base):
    __tablename__ = "students"

    stu_no: Mapped[str] = mapped_column(String(10), primary_key=True)
    stu_name: Mapped[str] = mapped_column(String(255), nullable=False)
    stu_class: Mapped[str] = mapped_column(String(255), nullable=False)
    stu_phone: Mapped[str] = mapped_column(String(10), nullable=False)

    def __repr__(self):
        return f"<Student(stu_no='{self.stu_no}', stu_name='{self.stu_name}', stu_class='{self.stu_class}', stu_phone='{self.stu_phone}')>"

# Create a tkinter window
window = tkinter.Tk()
window.title("查詢並修改學生資料")

# Create a connection to the database
engine = create_engine(f'mysql+mysqlconnector://root:{os.environ["MYSQL_PASSWORD"]}@localhost/example_sa')
session = Session(engine)

# Allow users to input a student number
id_input_frame = Frame(window)
id_input_frame.pack(padx=10, pady=10)

id_input_entry_frame = Frame(id_input_frame)
id_input_entry_frame.pack()
stu_no_label = Label(id_input_entry_frame, text="學號")
stu_no_label.grid(row=0, column=0)
stu_no_entry = Entry(id_input_entry_frame)
stu_no_entry.grid(row=0, column=1)
stu_query_btn = Button(id_input_frame, text="查詢")
stu_query_btn.pack()

# Show the student data
stu_data_frame = Frame(window)
stu_data_frame.pack(padx=10, pady=10)
stu_input_frame = Frame(stu_data_frame)
stu_input_frame.pack()
stu_name_label = Label(stu_input_frame, text="姓名")
stu_name_label.grid(row=0, column=0)
stu_name_entry = Entry(stu_input_frame)
stu_name_entry.grid(row=0, column=1)
stu_class_label = Label(stu_input_frame, text="班級")
stu_class_label.grid(row=1, column=0)
stu_class_entry = Entry(stu_input_frame)
stu_class_entry.grid(row=1, column=1)
stu_phone_label = Label(stu_input_frame, text="電話")
stu_phone_label.grid(row=2, column=0)
stu_phone_entry = Entry(stu_input_frame)
stu_phone_entry.grid(row=2, column=1)
stu_modify_btn_frame = Frame(stu_data_frame)
stu_modify_btn_frame.pack()
stu_update_btn = Button(stu_modify_btn_frame, text="修改")
stu_update_btn.grid(row=0, column=0)


current_selected_student: str | None = None

def select() -> None:
    global current_selected_student

    current_selected_student = stu_no_entry.get()
    student = session.get(Student, current_selected_student)

    # Write student's value to the entry
    if student:
        stu_name_entry.delete(0, tkinter.END)
        stu_name_entry.insert(0, student.stu_name)
        stu_class_entry.delete(0, tkinter.END)
        stu_class_entry.insert(0, student.stu_class)
        stu_phone_entry.delete(0, tkinter.END)
        stu_phone_entry.insert(0, student.stu_phone)
    else:
        tkinter.messagebox.showinfo("查詢", "查無此學生")
        current_selected_student = None


def update() -> None:
    global current_selected_student

    if current_selected_student is None:
        tkinter.messagebox.showerror("修改", "請先查詢學生")
        return

    student = session.get(Student, current_selected_student)

    try:
        assert student is not None
        student.stu_name = stu_name_entry.get()
        student.stu_class = stu_class_entry.get()
        student.stu_phone = stu_phone_entry.get()
        session.commit()
        tkinter.messagebox.showinfo("修改", "修改成功")
    except AssertionError:
        tkinter.messagebox.showerror("修改", "查無此學生")
    except SQLAlchemyError as e:
        tkinter.messagebox.showerror("修改", f"修改失敗: {e}")

stu_query_btn.bind("<Button-1>", lambda event: select())
stu_update_btn.bind("<Button-1>", lambda event: update())

window.mainloop()
