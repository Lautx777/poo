#Crea una clase Coche con atributos como marca, modelo y año. 
#Luego, arma un método que imprima la información del coche y otro método que acelere el coche.
#Esta clase posee pura y exclusivamente atributos publicos (cualquiera puede acceder y modificarlos)
class Coche:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year 
        self.acceleration = 0
        
    def info(self):
        print(f"El auto es de marca {self.brand}, modelo {self.model} del year {self.year}, y va a {self.acceleration} km/h")
        
    def accelerar(self, cuanto):
        self.acceleration = cuanto 
            
        
car = Coche("Audi", "2.0", 2020)
car.info()
car.accelerar(200)        
car.info()    
car.acceleration = 120
car.info()