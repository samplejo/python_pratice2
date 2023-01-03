#using tuple
t=tuple()
print(type(t))
print(t)
t1=6,7,8,9,0
print(type(t1))
print(t1)
print(t1[2])
for i in t1:
    print(i**2)
#using range
t2=tuple(range(0,11,1))
print(t2)
l=[1,2,3,4]
t3=tuple(l)
print(t3)
t4=(777,)
print(type(t4))
print(t4)
t5=(888,)
print(type(t5))
print(t5)
#packing
p=40
q=360
r=365
t5=p,q,r
print(t5)
#unpacking
x,y,z=t5
print(x)
print(y)
print(z)

