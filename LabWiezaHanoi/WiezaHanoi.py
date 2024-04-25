counter = 0
def Hanoi(n, source, destination, buff):
    global counter
    counter += 1
    if n == 1:
        print("Move disk (n==1)", source[-1], "from source ", source, " to destination ", destination)
        destination.append(source.pop())
        print('Source ', source)
        print('Buff ', buff)
        print('Destination ', destination)
    else:
        Hanoi(n-1, source, buff, destination)
        print("Move disk ", source[-1], "from source ", source, " to buff ", destination)
        destination.append(source.pop())
        print('Source ', source)
        print('Buff ', buff)
        print('Destination ', destination)
        Hanoi(n-1, buff, destination, source)
    return counter
Source = [4,3,2,1]
Buff = []
Destination = []

print(Hanoi(len(Source), Source, Buff, Destination))

