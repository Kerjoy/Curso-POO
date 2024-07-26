class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_data(self):
         print(f"Name:{self.name}")
         print(f"Age:{self.age}")
    
class Student(People):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
        
    def show_grade(self):
         print(f"Grade:{self.grade}")

student_1 = Student("Juan","21","8")
student_1.show_data()
student_1.show_grade()