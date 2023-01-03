import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
l=list()
print(type(l))
print(l)
l=[1,2,3,4,100,11,'A','B','Z',"Banglore",True]
print(l)
print(l[6])
for i in l:
    print(i)
l1=list(range(1,11))
print(l1)
l2=list(range(0,11,2))
print(l2)
l.clear()
print(l)
del l
#print(l)
print(len(l1))
l=[1,2,3,4]
print(l)
l.append(10)
print(l)
l.insert(2,222)
print(l)
l1=[111,555,777]
l.extend(l1)
print(l)
l.remove(2)
print(l)
l.pop()
print(l)
l.pop(1)
print(l)
prime_numbers=[2,5,8,9]
prime_numbers.reverse()
print('Reversed List:',prime_numbers)
l=[12,1,33,99,56,3000,67,3,88888]
l.sort()
print(l)
l=["A","s","D","z","johnSon valloor  jose"]
l.sort()
print(l)
