f = open('zadanie2.csv', 'r')
f2 = open("delWords.txt", "w")
lineRead = f.readline()
f2.write(lineRead)

l = []

for line in f:
    line = line.strip("\n").split(",")
    if line[1] != '':
        l.append([int(line[0]), line[1]])

l.sort()

i = 1
for elements in l:
    elements[1] = elements[1].lower()
    elements[0] = i
    i += 1

for i in range(len(l)):
    for word in l[i][1].split():
        if len(word) > 1 and abs(ord(word[0]) - ord(word[1])) == 1:
            l[i][1] = l[i][1].replace(word, '')
            f2.write(str(l[i][0]) + ', ' + str(word) + '\n')

f.close()
f2.close()
print(l)
