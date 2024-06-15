class student:
    def __init__(self,name,old,grade):
        self.name = name
        self.old = old
        self.grade = grade

    def studyng():
        print("studyng...")


name = input("introduce your name please: ")
old = input("introduce your name old: ")
name = input("introduce your name grade: ")

student1 = student(name,old,name)

print(f"""
     STUDENT DATA: \n\n
     Name: {student1.name} \n
     Edad: {student1.old} \n
     Grade: {student1.grade} \n
    """)
while 1:
    studyng = input()
    if (studyng.lower() == "studyng"):
        student.studyng()