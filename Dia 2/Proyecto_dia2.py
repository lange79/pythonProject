nombre= input("Ingresa tu Nombre: ")
apellido= input("Ingresa tu Apellido: ")
ventas= int(input("ingresa el importe total de ventas: "))
comisiones=round(ventas*0.13,2)
print(f"Las comisiones por ventas de {nombre} {apellido} son de {comisiones}")