mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)

mi_set = set({1,2,3,4,5})
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#mi_set[0]=5

mi_set = set((1,2,3,4,5,1,1,1,2,3,2))
print(type(mi_set))
print(mi_set)

#mi_set = set((1,2,3,4,[2,1],1,1,1,2,3,2))
#print(type(mi_set))
#print(mi_set)

mi_set = set((1,2,3,4,(1,2,3),1,1,1,2,3,2))
print(type(mi_set))
print(mi_set)

mi_set = set({1,2,3,4,5})
print(len(mi_set))
print(mi_set)

mi_set = set({1,2,3,4,5})
print(2 in mi_set)

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

s1={1,2,3}
s1.add(4)
print(s1)

s1={1,2,3}
s1.add(2)
print(s1)

s1={1,2,3}
s1.remove(3)
print(s1)

#s1={1,2,3}
#s1.remove(4)
#print(s1)

s1={1,2,3}
s1.discard(3)
print(s1)

s1={1,2,3}
s1.discard(4)
print(s1)

s1={1,2,3}
s1.pop()
print(s1)

s1={1,2,3,4,5,6,7,8,9,10}
sorteo=s1.pop()
print("Los numeros a sortear son:",s1)
print("El numero sorteado es:",sorteo)

s1={1,2,3}
s1.clear()
print(s1)