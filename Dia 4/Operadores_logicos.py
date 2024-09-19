mi_bool=4<5<6
print(mi_bool)

mi_bool=4<5 and 5>6
print(mi_bool)

mi_bool=4<5 and 5==2+3
print(mi_bool)

mi_bool= 55==55 and "perro"=="perro"
print(mi_bool)

mi_bool=1==10 or 3==3
print(mi_bool)

mi_bool=1==10 or 3==1
print(mi_bool)

texto ="Esta frase es breve"
mi_bool="frase" in texto
print(mi_bool)
mi_bool="frase" in texto and ("python" in texto)
print(mi_bool)

mi_bool= not "a" == "a"
print(mi_bool)

mi_bool= not "a" != "a"
print(mi_bool)