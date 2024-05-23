import math
import time

def allCities():
    map = open('TSP.txt', 'r')
    data = map.read()
    lines = list(data.split('\n'))
    data =[]

    for line in lines:
        data.extend(line.split('\t'))
    print(data)

    totalDistance = 0
    startingCity = 7
    start = (startingCity-1)*3

    for i in range(start + 2, int((len(data)))):
        if i%3 == 0:
            if i == 300:
                squares1 = (float(data[i - 2]) - float(data[1])) ** 2
                squares2 = (float(data[i - 1]) - float(data[2])) ** 2
                distance = math.sqrt(squares1 + squares2)
                print('Distance between ', data[i - 3], ' and ', data[0], ' is ', distance)
            else:
                squares1 = (float(data[i-2]) - float(data[i + 1])) ** 2
                squares2 = (float(data[i-1]) - float(data[i + 2])) ** 2
                distance = math.sqrt(squares1 + squares2)
                print('Distance between ', data[i-3], ' and ', data[i], ' is ', distance)
            totalDistance += distance

    if startingCity != 1:
        for j in range(3, start+3):
            if j % 3 == 0:
                squares1 = (float(data[j - 2]) - float(data[j + 1])) ** 2
                squares2 = (float(data[j - 1]) - float(data[j + 2])) ** 2
                distance = math.sqrt(squares1 + squares2)
                print('Distance between ', data[j - 3], ' and ', data[j], ' is ', distance)
                totalDistance += distance

    return totalDistance


def parse_input_file(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')

    cities = []
    for line in data:
        parts = line.split('\t')
        city_id = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
        cities.append((city_id, x, y))

    return cities


def euclidean_distance(city1, city2):
    return math.sqrt((city1[1] - city2[1]) ** 2 + (city1[2] - city2[2]) ** 2)


def greedy_tsp(cities, starting_city_id):
    n = len(cities)
    visited = [False] * n
    path = []
    total_distance = 0

    current_city_index = starting_city_id - 1
    path.append(cities[current_city_index][0])
    visited[current_city_index] = True

    for _ in range(n - 1):
        next_city_index = None
        min_distance = float('inf')

        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city_index], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city_index = i

        visited[next_city_index] = True
        total_distance += min_distance
        path.append(cities[next_city_index][0])
        current_city_index = next_city_index


    total_distance += euclidean_distance(cities[current_city_index], cities[starting_city_id - 1])
    path.append(cities[starting_city_id - 1][0])

    return path, total_distance


def nearest_neighbor(cities, starting_city_id):
    n = len(cities)
    visited = [False] * n
    path = []
    total_distance = 0

    current_city_index = starting_city_id - 1
    path.append(cities[current_city_index][0])
    visited[current_city_index] = True

    for _ in range(n - 1):
        next_city_index = None
        min_distance = float('inf')

        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city_index], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city_index = i

        visited[next_city_index] = True
        total_distance += min_distance
        path.append(cities[next_city_index][0])
        current_city_index = next_city_index


    total_distance += euclidean_distance(cities[current_city_index], cities[starting_city_id - 1])
    path.append(cities[starting_city_id - 1][0])

    return path, total_distance


def calculate_total_distance(cities, path):
    total_distance = 0
    for i in range(len(path) - 1):
        city1 = cities[path[i] - 1]
        city2 = cities[path[i + 1] - 1]
        total_distance += euclidean_distance(city1, city2)
    return total_distance


def two_opt(cities, path):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if j - i == 1: continue
                new_path = path[:i] + path[i:j][::-1] + path[j:]
                if calculate_total_distance(cities, new_path) < calculate_total_distance(cities, path):
                    path = new_path
                    improved = True
    return path


# For two_opt
print('For two_opt algorithm')
stime = time.time()
cities = parse_input_file('TSP.txt')
starting_city_id = 7

path, _ = nearest_neighbor(cities, starting_city_id)
optimized_path = two_opt(cities, path)
total_distance = calculate_total_distance(cities, optimized_path)

print("Time is ", time.time() - stime)
print("Optimized path:", optimized_path)
print("Total distance:", total_distance)
print()

# For greedy algorithm
print('For greedy algorithm')
stime1 = time.time()
cities = parse_input_file('TSP.txt')
starting_city_id = 7
path, total_distance = greedy_tsp(cities, starting_city_id)
print("Time is ", time.time() - stime1)
print("Shortest path:", path)
print("Total distance:", total_distance)

print()
# For order in file TSP.txt
print('For order in file TSP.txt algorithm')
stime2 = time.time()
x = allCities()
print("Time is ", time.time() - stime2)
print('Total distance is: ', x)
