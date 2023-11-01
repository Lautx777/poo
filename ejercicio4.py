#Crea una clase Libro con atributos como título, autor y año de publicación. 
#Definir un método para imprimir la información del libro. 

class Book:
    def __init__(self, tittle, author, year):
        self.tittle = tittle
        self.author = author
        self.year = year
    
    def info(self):
      print(f"Nombre del libro: {self.tittle}, Author: {self.author}, Year: {self.year}")
      
      
book = Book("Rojo al mar", "Juan", "1970")  
book.info()    
    

