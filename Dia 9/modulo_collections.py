from collections import Counter

numeros =[7,8,8,9,0,7,6,6,5,4,3,7,5,8,]
frase = "Al pan pan y al vino vino"

print(Counter("Mississipi"))
print(Counter(numeros))
print(Counter(frase))
print(Counter(frase.split()))
print("\n")

serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4])

print(serie.most_common())
print(serie.most_common(2))
print(list(serie))

print("*"*25)


from collections import defaultdict

mi_dic ={"uno":"verde","dos":"azul","tres":"rojo"}

print(mi_dic['dos'])

mi_dic2=defaultdict(lambda:"nada")
mi_dic2["uno"]="verde"

print(mi_dic2['dos'])
print(mi_dic2)
print("*"*25)

from collections import namedtuple

mi_tupla=(600,18,65)

print(mi_tupla[1])

Persona = namedtuple("Persona", ["Nombre","Altura", "Peso"])
ariel = Persona("Ariel", 1.76, 79)

print(ariel.Nombre)
print(ariel.Altura)
print(ariel.Peso)

print(ariel[0])


