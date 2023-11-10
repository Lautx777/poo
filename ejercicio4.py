#Crea una clase Libro con atributos como título, autor y año de publicación. 
#Definir un método para imprimir la información del libro. 

class Book:
    def __init__(self, tittle, author, year): #atributos de la clase 
        self.tittle = tittle  #asignacion de los atributos O PROPIEDADES
        self.author = author  #asignacion de los atributos O PROPIEDADES 
        self.year = year      #asignacion de los atributos O PROPIEDADES
    
    def info(self):  #definicion de un metodo
      print(f"Nombre del libro: {self.tittle}, Author: {self.author}, Year: {self.year}") #cuerpo del metodo
      
      
book = Book("Rojo al mar", "Juan", "1970")  #instanciacion de una clase, es en el MOMENTO que una clase pasa a ser un objeto.
book.info()    
    

