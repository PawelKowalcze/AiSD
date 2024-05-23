import math
import itertools

def read_coordinates(file_path):
    coordinates = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            city_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            coordinates[city_id] = (x, y)
    return coordinates

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def iterating_through_patch(path, coordinates):
    total_length = 0
    for i in range(len(path) - 1):
        city1 = path[i]
        city2 = path[i + 1]
        total_length += euclidean_distance(coordinates[city1], coordinates[city2])
    # Add distance from last city back to the first city
    total_length += euclidean_distance(coordinates[path[-1]], coordinates[path[0]])
    return total_length

def greedy_tsp(coordinates):
    num_cities = len(coordinates)
    unvisited = set(coordinates.keys())
    current_city = list(coordinates.keys())[0]
    path = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to the starting city
    path.append(path[0])
    return path


def two_opt_swap(path, i, k):
    new_path = path[0:i]
    new_path.extend(reversed(path[i:k + 1]))
    new_path.extend(path[k + 1:])
    return new_path


def two_opt(coordinates):
    path = list(coordinates.keys())
    path.append(path[0])  # Start and end at the same city
    improved = True

    while improved:
        improved = False
        best_distance = iterating_through_patch(path, coordinates)
        for i in range(1, len(path) - 2):
            for k in range(i + 1, len(path) - 1):
                new_path = two_opt_swap(path, i, k)
                new_distance = iterating_through_patch(new_path, coordinates)
                if new_distance < best_distance:
                    path = new_path
                    best_distance = new_distance
                    improved = True
    return path


if __name__ == '__main__':
    file_path = 'TSP.txt'
    coordinates = read_coordinates(file_path)

    for i in coordinates.items():
        print(i)


    # Calculate the total length of the path using the iterating_through_file function
    path = list(coordinates.keys()) # tutaj ścieżka to kolejne miasta w pliku
    total_length = iterating_through_patch(path, coordinates)
    print(f"The total length of the path is: {total_length}")

    # Wybiurcza ścieżka, najbliższe miasto
    path_greedy = greedy_tsp(coordinates)
    total_length_greedy = iterating_through_patch(path, coordinates)
    print(f"The path is: {path_greedy}")
    print(f"The total length of the greedy path is: {total_length_greedy}")


    #2-opt Heuristic Algorithm
    path_two_opt = two_opt(coordinates)
    total_length_two_opt = iterating_through_patch(path_two_opt, coordinates)
    print(f"The path is: {path_two_opt}")
    print(f"The total length of the 2-opt path is: {total_length_two_opt}")









