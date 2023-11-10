class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Vaca(Animal):
    def hacer_sonido(self): 
        return "Muu"

# Uso del polimorfismo
animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    print(f"Este animal hace: {animal.hacer_sonido()}")
