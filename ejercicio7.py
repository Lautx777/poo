#Herencia:
#Llevar el concepto de herencia a objetos personas

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        print(f"Conduciendo {self.marca} {self.modelo}")

class Coche(Vehiculo):
    def cantidad_ruedas(self):
        print(f"Tiene 4 ruedas")
    def abrir_maletero(self):
        print(f"Abriendo el maletero del {self.marca} {self.modelo}")

class Moto(Vehiculo):
    def cantidad_ruedas(self):
        print(f"Tiene 2 ruedas")
    def poner_casco(self):
        print("Poniéndose el casco")

# Uso de las clases con herencia
mi_coche = Coche("Toyota", "Camry")
mi_coche.conducir()
mi_coche.cantidad_ruedas()
mi_coche.abrir_maletero()

mi_moto = Moto("Honda", "CBR")
mi_moto.conducir()
mi_moto.poner_casco()
mi_moto.cantidad_ruedas()

