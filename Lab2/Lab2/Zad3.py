import time
f = open("SJP.txt", "r")

x = input('Write any text: ')
if len(x.split(' ')) == 1:
    print('Your text is one word')

stime = time.time()

is_word = False
x = x.lower()
for line in f:
    if x == line.strip():
        is_word = True
        break

if is_word:
    print('Your text is a real word')
else:
    print('Your text is not a real word')

print(x)
print(time.time() - stime)