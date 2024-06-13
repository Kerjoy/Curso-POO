class student:
    def __init__(self,name,old,grade):
        self.name = name
        self.old = old
        self.grade = grade
        
    def studyng(self):
        print("Estudyng...")
        
pedro = student("MR CROC",24,100)

name = input("introduce your name please: ")
old = input("introduce your name old: ")
name = input("introduce your name grade: ")

student1 = student(name,old,name)

print(f"""
     STUDENT DATA: \n\n
     Name: {student.name} \n
     Edad: {student.old} \n
     Grade: {student.grade} \n
    
    """)

studyng = input()