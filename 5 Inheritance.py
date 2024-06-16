class People:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def speak(self):
        print("Hi, how are you?")
class Worker(People):
    def __init__(self, name, age, nationality,work,salary):
        super().__init__(name,age,nationality)
        self.work = work
        self.salary = salary

robert = Worker("Robert","42","Alien","Dragon People","100 000")

#print(robert.speak())
print(robert.salary)

