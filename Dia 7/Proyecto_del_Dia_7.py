class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return  f"Cliente: {self.nombre} {self.apellido} \n Balance de cuenta {self.numero_cuenta}: ${self.balance}"


    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Desposito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro Realizado")
        else:
            print("Fondos Insuficientes")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su Apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente=Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion=0
    while opcion != 'S':
        print("Elije : Deposuitar (D), Retirar (R), o Salir (S)")
        opcion = input()
        if opcion== 'D':
            monto_dep = int(input("Monto a Depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion =='R':
            monto_ret = int(input("Monto a Retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en bacno Python")

inicio()


