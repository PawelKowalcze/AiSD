numbers = ''
for i in range(500,3001):
    if i % 7 == 0 and i % 5 != 0:
        numbers += str(i)
print(numbers)

print(numbers.count('21'))
print(numbers.replace('21', 'XX'))
