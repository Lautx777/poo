# Herencia:
# Llevar el concepto de herencia a objetos personas

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, soy una persona!")
        
    def age(self):
        if self.__edad < 18:
            print(f"Eres un estudiante")
        else:
            print("Eres un trabajador")    


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)  
        self.__trabajo = trabajo
        self.__salario = salario 
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.__notas = notas
        self.__universidad = universidad         


persona1 = Empleado("Juan", 26, "uruguayo", "developer", 100)
persona1.hablar()
persona1.age()


persona2 = Estudiante("Agustin", 15, "uruguayo", 10, "FADU")
persona2.hablar() 
persona2.age()