from array import *

print("Hello World!")

a = 10
b = 2.7
c = 'abc'
d = True
e = 2 + 1j * 3

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(a + b)
print(str(a) + c)

persons = ['Tom', 'John', 'Smith']
print(persons)
print(persons[1])
print(persons[-1])
print(persons[:1])
print(persons[-1:])
print(persons[0:2])
print(len(persons))
persons.append(123)
print(persons)
print(persons[3])
persons.remove(123)
print('Mark' in persons)
print(persons * 2)
print(persons + ['Mark'])

a = [1, 2, 3, 5]
print(1 in a)
print(a.pop())
print(a)
print(a.pop(0))  # pop(index of element)
print(a)
a.append([1, 3, 5, 5, 4])
print(a)
print(a.count(2))

ages = {'Tom': 20, 'John': 19, 'Smith': 10}
print(ages['John'])

record = {
    'Name': 'Mark',
    'Age': 63
}

print(record)
print(record['Name'])
record['Name'] = 'Lucy'
record['Age'] = 25
print(record)

x = array('f', [1, 2, 3])
print(x)
print(x[0])
print(type(x))

y = int(input('Insert text: '))
print(type(y))

l = ['a', 'b', 'c', 3]
for i in l:
    print(i)

