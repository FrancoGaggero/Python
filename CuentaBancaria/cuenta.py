#Clase Cuenta Bancaria
#Clase CuentaBancaria con atributos: titular, saldo.
#Métodos: depositar(monto), retirar(monto) y mostrar_saldo().
#Controla que no se pueda retirar más dinero del disponible.
import datetime


class cuenta:
    def __init__(self, titular, saldo=0.0, movimiento = []):
        self.titular = titular
        self.saldo = saldo
        self.movimiento = movimiento





    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular
    
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_movimiento(self):
        return self.movimiento
    
    def set_movimiento(self, movimiento):
        self.movimiento = movimiento




    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            movimiento = f"Depósito: +${monto:.2f}"
            self.movimiento.append(movimiento)
            print(f"Depósito exitoso de ${monto:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")


    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes para retirar esa cantidad.")
        elif monto <= 0:
            print("El monto a retirar debe ser positivo.")
        else:
            self.saldo -= monto
            movimiento = f"Retiro: -${monto:.2f}"
            self.movimiento.append(movimiento)
            print(f"Retiro exitoso de ${monto:.2f}. Nuevo saldo: ${self.saldo:.2f}")



    def verMonto(self):
        print(f"El saldo actual es: ${self.saldo:.2f}")
        return self.saldo
    

    def verMovimientos(self):
        if not self.movimiento:
            print("No hay movimientos para mostrar.")
        else:
            print("Movimientos de la cuenta:")
            for mov in self.movimiento:
                print(mov)
        return self.movimiento

    