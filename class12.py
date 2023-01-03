t=tuple()
print(type(t))
print(t)
t1=1,2,3,4,5
print(type(t1))
print(t1)
print(t1[4])
for i in t1:
    print(i**2)
t2=tuple(range(0,11,2))
print(t2)
l=[1,2,3,4]
t3=tuple(l)
print(t3)
t4=(111,)
print(type(t4))
print(t4)
t5=(222,)
print(type(t5))
print(t5)
#packing and unpacking of tuple
#packing
a=20
b=30
c=40
t5=a,b,c
print(t5)
#unpacking
p,q,r=t5
print(p)
print(q)
print(r)
#creating dictionary
d={}
print(type(d))
print(d)
d1=dict()
print(d1)
d3={"name":"ram","age":22,"city":"banglore"}
print(d3)
d3["Salary"]=50000
print(d3)
print(d3["name"])
d3["city"]="delhi"
print(d3)
for key,value in d3.items():
    print(key,value)
print(d3.items())
print(d3.keys())
print(d3.values())
print(len(d3))
#print(d3["address"])
value=d3.get("age")
print(value)
value=d3.get("address")
print(value)
value=d3.get("address","no value")
print(value)
