def contar_primos(numero):
    primos=[]
    cant_primos=0
    cont_div=0
    for elemento in range(2,numero+1):
        div=2
        while elemento>=div:
            if elemento%div==0:
                cont_div+=1
            div+=1
        if cont_div==1:
            cant_primos+=1
            primos.append(elemento)
        cont_div=0
    return cant_primos,primos



dato=int(input("Ingrese el numero para buscar nros primos"))
cantidad, primos=contar_primos(dato)
print(f"La cantidad de nros primos que hay desde 1 a {dato} es:", cantidad)
print("La lista de nros Primos es:", primos)