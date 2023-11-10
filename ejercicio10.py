# Crea una clase base Animal con un método hacer_sonido.
# Luego, crear subclases como Perro, Gato y Vaca que van a sobreescribir el método hacer_sonido para producir sonidos diferentes.

class Animal():
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Woof"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"


mis_animales = [Perro(), Gato(), Vaca()]
for animal in mis_animales:
    print(f"Este animal hace: {animal.hacer_sonido()}")
    
    
