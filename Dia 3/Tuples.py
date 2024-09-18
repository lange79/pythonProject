mi_tuple = (1,2,3,4)
print(type(mi_tuple))

mi_tuple = 1,2,3,4
print(type(mi_tuple))

t = (5,6,7,'fff')
print(type(t))
print(mi_tuple[2])
print(t[-2])
#mi_tuple[1]=5

mi_tuple=(1,2,('a','b'),4)
print(mi_tuple[2])
print(mi_tuple[2][0])
mi_tuple=list(mi_tuple)
print(type(mi_tuple))
mi_tuple=tuple(mi_tuple)
print(type(mi_tuple))


t=(1,2,3)
x,y,z=t
print(x,y,z)

#,y,z,a=t
#print(x,y,z)
t=(1,2,3,1)
print(len(mi_tuple))

print(t.count(1))
print(t.count(2))
print(t.count(4))

print(t.index(2))






