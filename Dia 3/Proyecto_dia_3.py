texto=input("Ingrese Texto a Analizar:").lower()
l1,l2,l3=input ("Ingrese 3 letras:").lower()
lista=list(texto)


##############1####################
cantidad_l1=lista.count(l1)
cantidad_l2=lista.count(l2)
cantidad_l3=lista.count(l3)

##############2#####################
palabras=texto.split()
cant_palabras=len(palabras)

##############3#####################
primer_palabra=palabras[0]
ultima_palabra=palabras[-1]
primer_letra=primer_palabra[0]
ultima_letra=ultima_palabra[-1]

#############4#######################
palabras_r=palabras
palabras_r.reverse()
t=" ".join(palabras)

#############5#######################

p=str('python' in palabras)
dic={'True':"La palabra Python se encuentra en el texto",'False':"La palabra Python no se encuentra en el texto"}

##################Respuestas##################

print(f"La cantidad de veces que aparece la letra {l1} es:", cantidad_l1)
print(f"La cantidad de veces que aparece la letra {l2} es:", cantidad_l2)
print(f"La cantidad de veces que aparece la letra {l3} es:", cantidad_l3)

print("La cantidad de palabras en el texto es:", cant_palabras)

print("La primer letra del texto es:", primer_letra)
print("La ultima letra del texto es:", ultima_letra)

print("El texto con las palabras invertidas es:",t)

print(dic[p])




