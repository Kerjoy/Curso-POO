"""
Polymorphism: hace referencia a poder enviar un mensaje sintactico a diferentes objetos
el mensaje es el mismo pero el resultado es diferente, basicamente es hace que cuando nosotros
le demos un metodo a un objeto se comporte diferente.

las variables en python son polimorfas conocidas como polimorfismo en tiempo de ejecucion
"""
class Animal():
    def sonido(self):
        pass

class Cat(Animal):
    def sound(self):
        return"Miau"

class Dog(Animal):
    def sound(self):
        return"Guau"
    
gato = Cat()
perro = Dog()

def make_sound(animal):
    print(animal.sound())

make_sound(perro) #example polymorphism

print(perro.sound())  #example polymorphism

#polymorphism inheritance
