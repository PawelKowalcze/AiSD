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

a = [1, 2]
print(1 in a)
print(a.pop())
