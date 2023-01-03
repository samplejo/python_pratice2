#creating dictionary
d={}
print(type(d))
print(d)
#using dict function
d1=dict()
print(d1)
d3={"name":"jo","age":24,"city":"banglore"}
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
value=d3.get("age")
print(value)
value=d3.get("address")
print(value)
value=d3.get("address","no value")
print(value)
