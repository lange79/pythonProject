def remueve_repe (palabra):
    sinrepetir=set(palabra)
    sinrepetir=sorted(sinrepetir)
    return(sinrepetir)



print(remueve_repe("entretenido"))