def devolver_distintos(n1,n2,n3):
    r=0
    suma=n1+n2+n3
    if suma>15:
        if n1>=n2:
            if n1>=n3:
                r=n1
            else:
                r=n3
        elif n2>=n3:
            r=n2
        else:
            r=n3
    elif suma<10:
        if n1<=n2:
            if n1<=n3:
                r=n1
            else:
                r=n3
        elif n2<=n3:
            r=n2
        else:
            r=n3
    else:
        if n1>=n2:
            if n1>=n3:
                if n2>=n3:
                    r=n2
                else:
                    r=n3
            else:
                r=n1
        else:
            if n2>=n3:
                if n1>=n3:
                    r=n1
                else:
                    r=n3
            else:
                r=n2


    print(type(n1))
    return r



resultado=devolver_distintos(1,4,2)
print(resultado)


def devolver_distintos (a,b,c):
    suma =a+b+c
    lista=[a,b,c]

    if suma > 15:
        return max(lista)
    elif suma<10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
print(devolver_distintos(3,2,7))

