import csv
import time
import numpy as np


def fits_in_knapsack(knapsack, width, height, x, y):
    if x + width > len(knapsack) or y + height > len(knapsack):
        return False
    for i in range(width):
        for j in range(height):
            if knapsack[x + i][y + j] != 0:
                return False
    return True


def place_in_knapsack(knapsack, width, height, x, y, item_id):
    for i in range(width):
        for j in range(height):
            knapsack[x + i][y + j] = item_id


def first_fit_decreasing(knapsack, items):
    total_value = 0
    item_id = 1

    # Sort items by value density in descending order
    items.sort(key=lambda item: item[4], reverse=True)

    for item in items:
        placed = False
        width, height = item[1], item[2]

        # Try to place item in its original orientation
        for x in range(len(knapsack)):
            for y in range(len(knapsack)):
                if fits_in_knapsack(knapsack, width, height, x, y):
                    place_in_knapsack(knapsack, width, height, x, y, item_id)
                    total_value += item[3]
                    placed = True
                    break
            if placed:
                break

        # Try to place item in rotated orientation
        if not placed:
            for x in range(len(knapsack)):
                for y in range(len(knapsack)):
                    if fits_in_knapsack(knapsack, height, width, x, y):
                        place_in_knapsack(knapsack, height, width, x, y, item_id)
                        total_value += item[3]
                        placed = True
                        break
                if placed:
                    break

        item_id += 1

    return knapsack, total_value


def main():
    output_file = open('FFDresults.csv', 'w')
    header = ['N', 'time', 'value', 'max_value']
    writer = csv.writer(output_file, dialect='excel')
    writer.writerow(header)

    for dimension in ['20', '100', '500', '1000']:
        start_time = time.time()
        with open('packages' + dimension + '.txt') as txt_file:
            packages = [line.split(',') for line in txt_file]
        # Remove header
        del (packages[0])
        del (packages[0])
        for package in packages:
            package[-1] = package[-1].strip()
        packages = [[int(field) for field in package] for package in packages]
        # Add a column to store the value density
        for package in packages:
            package.append(package[3] / (package[1] * package[2]))

        # Initialize empty knapsack
        knapsack_grid = np.zeros((int(dimension), int(dimension)), dtype=int)

        # Apply the First-Fit Decreasing algorithm
        knapsack_grid, total_value = first_fit_decreasing(knapsack_grid, packages)

        print(knapsack_grid)
        print("First-Fit Decreasing, " + dimension + ", " + str(time.time() - start_time))
        print("Total value collected:", total_value)

        # Calculate maximum possible value
        max_possible_value = sum(package[3] for package in packages)

        print("Max possible value:", max_possible_value)
        writer.writerow([dimension, time.time() - start_time, total_value, max_possible_value])

    output_file.close()


if __name__ == '__main__':
    main()