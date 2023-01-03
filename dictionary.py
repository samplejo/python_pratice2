d={"Name":"johnson valloor jose","Age":24,"city":"Banglore","Address":"kudlu"}
print(d)
d.popitem()
print(d)
d1=d
print(d1)
d2=d.copy()
print(d2)
del d["Name"]
print(d)
#setdefault
d={1:23,2:45}
v=d.setdefault(1,111)
print(v)
v=d.setdefault(5,111)
print(v)
print(d)
#update d1 to d2
d1={"name":"johnson v j","age":24,"city":"banglore"}
print(d1)
d2={"emp id":20887}
print(d2)
d1.update(d2)
print(d1)
t={}
print(type(t))
#creating set
s=set()
print(type(s))
s={1,2,3,4,5,6,1,2,3,9,10}
print(s)
s1=set(range(0,11,2))
print(s1)
s2=set([1,2,3,4,5,7,8,1,2,3])
print(s2)
#print(s2[2])
#adding element to set
s={8,9,2,1}
s.add(333)
print(s)
#update function
l=[1,2,3]
t=(111,222,444,555)
s={888,999,777}
s1=set()
s1.update(l,t,s)
print(s1)
