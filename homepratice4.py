d={"name":"jo","age":23,"city":"banglore"}
print(d)
d.popitem()
print(d)
d1=d
print(d1)
d2=d.copy()
print(d2)
del d["name"]
print(d)
#setdefault
d={1:22,2:55}
v=d.setdefault(7,777)
print(v)
v=d.setdefault(6,666)
print(v)
print(d)
#add d1 to d2
d1={"name":"johnny","age":33,"city":"banglore"}
print(d1)
d2={"emp id":4565617}
print(d2)
d1.update(d2)
print(d1)
t={}
print(type(t))
#creating set
s=set()
print(type(s))
s={1,2,4,888,54,3,9}
print(s)
s1=set(range(0,11,2))
print(s1)
s2=set([1,2,233,4,5,6,0])
print(s2)
#adding element to set
s={4,5,6,0}
s.add(990)
print(s)
#update function
l=[4,5,6]
t=(777,888,999)
s={222,333,111}
s1=set()
s1.update(s,t,l)
print(s1)
s1.update(t,l,s)
print(s1)
s1.update(l,t,s)
print(s1)

