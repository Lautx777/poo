#Crea una clase CuentaBancaria con atributos como titular, saldo y métodos para depositar y retirar dinero.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  
        self.saldo = saldo       
        
    def mostrarSaldo(self):
        print(f"Su saldo es: ${self.saldo}")
    
    def depositar(self, cuanto):
        self.saldo += cuanto
        
    def retirar(self, cuanto):
        if self.saldo < cuanto:
            print(f"Saldo insuficiente")
        else:   
            self.saldo -= cuanto
        
        
cuentaBancaria = CuentaBancaria("Juan", 100)
cuentaBancaria.mostrarSaldo()
cuentaBancaria.depositar(200)
cuentaBancaria.mostrarSaldo()
cuentaBancaria.retirar(500)
cuentaBancaria.retirar(200)
cuentaBancaria.mostrarSaldo()
        
        
        
     
        
    