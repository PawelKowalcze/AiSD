abc = 'lksd fjald hfsof hosa'
print(abc[0])
print(abc[-1])
print(abc[:-4])
print(abc[6:11])

print(len(abc))
print(abc.count('l'))
print(abc.split('f'))
print(abc.split(' ')[2].split('f'))

print('a' in abc)

text = 'ala ma kota'
print(text.capitalize())
print(text[1:7].capitalize())
print(text.islower())
print(text[3].isspace())
print(text[0:2].isalpha())
print(text.find('l'))  # index pierwszego wystąpienia
print(text.find('ma'))
print(text.count('a'))
print(text.count('a', 0, 4))
print(text.endswith('la'))

text_utf = text.encode('utf-8')
print(text_utf)
print(type(text_utf))

xyz = 'Lorem ipsum dolor sit amet'
x = xyz.split(' ')
print(x)
print('_'.join(x))
print(''.join(x))

print(xyz.replace('m', 'r'))


abc = 'dżdżownica'
print(abc.strip('nic'))

print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{0}, {1}, {2}'.format('a', 'b', 'c'))

from string import Template

s = Template('$who likes $what')
printable_s = s.substitute(who='tim', what='kung pao')
print(s)
print(printable_s)

d =dict(who='tim', what='kung pao')
x = Template('$who likes $what').safe_substitute(d)
print(x)

name = 'Elisa'
age = 12
txt = f'Hello, {name}, you are {age} years old.'
print(txt)

txt2 = (
    f'Hi, {name}.'
    f'You are {age + 3}.'
)
print(txt2)


f = open('text.txt', 'r')
print(f)
txt = f.read()
print(txt)
print('---')
print(txt.splitlines())
print('###')
print(f.readline())
print('***')
f.close()

f = open('text.txt', 'r')
print(f.readline())
f.close()

f = open('text.txt', 'r')
for line in f:
    print(line)

f.close()
print('---')
