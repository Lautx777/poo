#Crea una clase CuentaBancaria con atributos como titular, saldo y métodos para depositar y retirar dinero.
#Encapsulamiento:Modificar el ejercicio de la 
# cuenta bancaria para que los atributos de saldo y titular sean privados y solo puedan ser accedidos a través
# de métodos. #También, agrega un método para obtener el saldo. 
# #Esto demuestra cómo el encapsulamiento protege los datos.

#Encapsular una clase es privatizar los atributos de la misma, en python se hace agregando "__" delante de la propiedad.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  
        self.__saldo = saldo       
        
    def titular(self):
        return self.__titular
                 
    def mostrarSaldo(self):
        print(f"Su saldo es: ${self.__saldo}")
    
    def depositar(self, cuanto):
        self.__saldo += cuanto
        
    def retirar(self, cuanto):
        if self.__saldo < cuanto:
            print(f"Saldo insuficiente")
        else:   
            self.__saldo -= cuanto
        
        
cuentaBancaria = CuentaBancaria("Juan", 100)
cuentaBancaria.mostrarSaldo()
cuentaBancaria.depositar(200)
cuentaBancaria.mostrarSaldo()
cuentaBancaria.retirar(500)
cuentaBancaria.retirar(200)
cuentaBancaria.mostrarSaldo()
cuentaBancaria.titular()        
        
        
     
        
    