class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def study(self):
        print(f"the student {self.name} is studyng")

student_name = input("Introduce a name for student: ")
student_age = input("Introduce a age for student: ")
student_grade = input("Introduce a grade for student: ")
stud = student(student_name,student_age,student_grade)
stud.study()