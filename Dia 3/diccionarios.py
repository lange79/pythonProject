diccionario={'c1':'valor1','c2':'valor2'}
print(diccionario)
a='c1'
print(diccionario[a])
resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88, 'talla':1.76}
consulta = (cliente['talla'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])

print(dic['c3'])
print(dic['c3']['s2'])


dic = {'c1':['a','b','c'],'c2':['d','e','f']}
r=(dic['c2'][1])
print(r.upper())

dic={1:'a',2:'b'}
print(dic)

dic[3] ='c'
print(dic)

dic[2] ='B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

