#Crea una clase llamada Perro con atributos como nombre, edad y raza. Luego, define métodos para imprimir la información del perro y hacer que el perro ladre. 

class Dog:
    def __init__(self, name, age, raza):
        self.nombre = name
        self.edad = age
        self.raza = raza

    def info(self):
        print(f"El perro se llama {self.nombre}, tiene {self.edad} años y es de la raza {self.raza}")
    
    
    def ladrar(self):
        print(f"El perro {self.nombre} esta ladrando") 


        
#Dog es una clase
#Linea 20 instancia de un objeto, lo que esta entre () son atributos de instanciación.
perro = Dog("Juan", 20, "Perro")

#Estos son métodos que imprimen información en la consola
perro.ladrar()
perro.info()        