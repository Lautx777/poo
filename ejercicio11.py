from abc import abstractmethod


class Books():
    @abstractmethod
    
    def __init__(self, tittle, author, year):
        self.tittle = tittle 
        self.author = author
        self.year = year 
    
    def detalles(self):
        pass  
          
class FisicoBook(Books):  
    def __init__(self, tittle, author, year, peso):
        super().__init__(tittle, author, year)  
        self.peso = peso
    
    def detalles(self):
        print(f"Nombre del libro: {self.tittle}, Author: {self.author}, Year: {self.year}, Gr: {self.peso}") 
           
class ElectronicBook(Books):
    def __init__(self, tittle, author, year, url):
        super().__init__(tittle, author, year)
        self.url = url
    
    def detalles(self):
        print(f"Nombre del libro: {self.tittle}, Author: {self.author}, Year: {self.year}, URL: {self.url}")   
         
        
        
def MostrarDetalles(Books):
    Books.detalles()
    
lautaro = FisicoBook("Roma", "Pintor", 1200, 100)  #Instanciar un objeto
lautaro2 = ElectronicBook("Roma", "Pintor", 1200, "httpgoogle.com.uy") #Instanciar un objeto
lautaro3 = Books("Roma", "Pintor", 1200)

MostrarDetalles(lautaro)     
MostrarDetalles(lautaro2)