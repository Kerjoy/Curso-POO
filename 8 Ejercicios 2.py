class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
        
class Murcielago(Mamifero,Ave):
    pass
print("el ave esta:")
ave = Ave()
ave.comer()
ave.volar()
print("el murcielago esta:")
murcielago = Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()

print(Murcielago.mro())