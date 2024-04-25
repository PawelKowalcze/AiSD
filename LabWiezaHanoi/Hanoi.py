import time

counter = 0


# Rozwiązanie rekurencyjne

def recursiveHanoi(n, source, destination, buff):
    global counter
    counter += 1
    if n == 1:
        # print("Move disk (n==1)", source[-1], "from source ", source, " to destination ", destination)
        destination.append(source.pop())
        # print('Source ', source)
        # print('Buff ', buff)
        # print('Destination ', destination)
    else:
        recursiveHanoi(n - 1, source, buff, destination)
        # print("Move disk ", source[-1], "from source ", source, " to buff ", destination)
        destination.append(source.pop())
        # print('Source ', source)
        # print('Buff ', buff)
        # print('Destination ', destination)
        recursiveHanoi(n - 1, buff, destination, source)
    return counter


n = 30
Source = [i for i in range(n, 0, -1)]
Buff = []
Destination = []
stime = time.time()
print('Number of operations', recursiveHanoi(len(Source), Source, Destination, Buff))
print('Recursion time for', n, 'blocks ', time.time() - stime)

# Rozwiązanie iteracyjne
counter = 0


def iterHanoi(n, sour, dst, buff):
    global counter
    i = 1
    while (len(sour) != 0 or len(buff) != 0):
        if i % 3 == 1:
            if len(dst) != 0 and len(sour) != 0:
                if dst[-1] > sour[-1]:
                    dst.append(sour.pop())
                else:
                    sour.append(dst.pop())
                counter += 1
            elif len(dst) != 0 and len(sour) == 0:
                sour.append(dst.pop())
                counter += 1
            elif len(dst) == 0 and len(sour) != 0:
                dst.append(sour.pop())
                counter += 1
            #print(i)
            #print('Source ', sour)
            #print('Buff ', buff)
            #print('Destination ', dst)

        if i % 3 == 2:
            if len(sour) != 0 and len(buff) != 0:
                if sour[-1] > buff[-1]:
                    sour.append(buff.pop())
                else:
                    buff.append(sour.pop())
                counter += 1
            elif len(sour) != 0 and len(buff) == 0:
                buff.append(sour.pop())
                counter += 1
            elif len(sour) == 0 and len(buff) != 0:
                sour.append(buff.pop())
                counter += 1
            #print(i)
            #print('Source ', sour)
            #print('Buff ', buff)
            #print('Destination ', dst)
        if i % 3 == 0:
            if len(buff) != 0 and len(dst) != 0:
                if buff[-1] > dst[-1]:
                    buff.append(dst.pop())
                else:
                    dst.append(buff.pop())
                counter += 1
            elif len(buff) != 0 and len(dst) == 0:
                dst.append(buff.pop())
                counter += 1
            elif len(buff) == 0 and len(dst) != 0:
                buff.append(dst.pop())
                counter += 1
            #print(i)
            #print('Source ', sour)
            #print('Buff ', buff)
            #print('Destination ', dst)
        i += 1
        if len(dst) == n or len(buff) == n:
            return counter
    return counter


n = 30
Source = [i for i in range(n, 0, -1)]
Buff = []
Destination = []
stime = time.time()
print('Number of operations', iterHanoi(len(Source), Source, Destination, Buff))
print('Iteration time for', n, 'blocks ', time.time() - stime)