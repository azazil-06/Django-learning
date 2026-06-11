n=5
#print(id(n))
data="python programming"


l1=["app","hi","new"]
print(len(l1))

l1.append("grapes")
print(l1)

l1.insert(2,"pop")
print(l1)

#dictionary
person= {
    'name' : 'arj',
    'age' : 20

}

print(person)
print(person.keys())
print(person.values())

person.update({'phone' : 123456 ,})
print(person)
#person.pop({'phone'})
print(person)

#set
s1={'apple','mango','apple'}
print(s1)