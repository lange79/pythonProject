def vof (*args):
    cero=0
    for arg in args:
        if arg==0:
            cero+=1
            if cero==2:
                return True
        else:
            cero=0
    return False


print(vof(1,3,4,8,0,7,1,0,0,4))


def ceros_vecinos(*args):
    contador=0
    for num in args:
        if args[contador] == 0 and args[contador+1]==0:
            return True
        else:
            contador +=1
    return False

print(ceros_vecinos(1,3,4,8,0,7,1,3,0,4))