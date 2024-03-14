from tkinter import *

class Student:

    def __init__(self, name):
        self.name = name

    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade():
    current_cursor = students_listbox.curselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[current_student].get_grade())

csc_2 = []

csc_2.append(Student("Boaz"))
csc_2[0].set_grade("Achieved")
csc_2.append(Student("Rehaan"))
csc_2[1].set_grade("Merit")
csc_2.append(Student("Aaran"))
csc_2[2].set_grade("Excellence")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Boaz")
students_listbox.insert(0, "Rehaan")
students_listbox.insert(0, "AARAN")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()


