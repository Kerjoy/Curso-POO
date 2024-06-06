class cellphone:
    def __init__(self,brand, model,camera):
        self.brand = brand
        self.model = model
        self.camera = camera
        
cell1 = cellphone ("Samgung","S23","48MP")

print(cell1.brand)