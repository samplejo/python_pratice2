import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
l=list()
print(type(l))
print(l)
l=["johnson",True,False,1,2,44,555,'jvj']
print(l)
print(l[4])
for i in l:
    print(i)
#using range function
l1=list(range(1,10))
print(l1)
l2=list(range(0,11,1))
print(l2)
#using clear
l.clear()
print(l)
#using delete function
del l
#using length
print(len(l1))
l=[8,7,6,5]
print(l)
#using append
l.append(20)
print(l)
#using insert
l.insert(4,420)
print(l)
#using extend
l1=[420,840,1620]
l.extend(l1)
print(l)
#using remove
l.remove(5)
print(l)
#using pop
l.pop()
print(l)
l.pop(3)
print(l)
#using prime numbers and reverse
prime_numbers=[2,5,6,8,10]
prime_numbers.reverse()
print('Reveresed List:',prime_numbers)
#using sort
l=[999,2,1,88,4435,787585555765,0]
l.sort()
print(l)
l=["ABc","d","Johnson"]
l.sort()
print(l)

