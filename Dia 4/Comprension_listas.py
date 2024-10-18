palabra = 'python'

lista=[]
for letra in palabra:
    lista.append(letra)
print(lista)



lista=[letra for letra in palabra]
print(lista)

lista=[letra for letra in 'python']
print(lista)

lista=[n for n in range(0,21,2)]
print(lista)

lista=[n/2 for n in range(0,21,2)]
print(lista)


lista=[n for n in range(0,21,2) if n*2>10]
print(lista)

lista=[n if n*2>10 else 'no' for n in range(0,21,2)]
print(lista)


pies = [10,20,30,40,50]
metros=[p/3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado=[vc**2 for vc in valores]
print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[vp for vp in valores if vp%2==0]

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(f-32)*(5/9) for f in temperatura_fahrenheit]
print(grados_celsius)