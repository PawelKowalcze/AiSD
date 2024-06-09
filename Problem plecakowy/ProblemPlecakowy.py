import csv
import time
import numpy as np

# Greedy algorithm
def can_fit(width, height, knapsack_grid):
    for width_start in range(len(knapsack_grid) - width + 1):
        for height_start in range(len(knapsack_grid) - height + 1):
            fits = True
            for width_iter in range(width):
                for height_iter in range(height):
                    if knapsack_grid[width_start + width_iter][height_start + height_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return width_start, height_start, False
    # Check if it fits after rotation
    for width_start in range(len(knapsack_grid) - width + 1):
        for height_start in range(len(knapsack_grid) - height + 1):
            fits = True
            for width_iter in range(width):
                for height_iter in range(height):
                    if knapsack_grid[height_start + height_iter][width_start + width_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return width_start, height_start, True

    return False

def main():
    output_file = open('results.csv', 'w')
    header = ['N', 'time', 'value', 'max_value']
    writer = csv.writer(output_file, dialect='excel')

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

        # Sort by value density in descending order
        packages.sort(key=lambda x: -x[4])

        # Initialize empty knapsack
        knapsack_grid = np.zeros((int(dimension), int(dimension)), dtype=int)
        total_value = 0
        placement_count = 0

        for package in packages:
            placement = can_fit(package[1], package[2], knapsack_grid)
            if placement:
                placement_count += 1

                # Place in knapsack with rotation
                if placement[2]:
                    for width in range(placement[0], package[1] + placement[0]):
                        for height in range(placement[1], package[2] + placement[1]):
                            knapsack_grid[height][width] = placement_count
                # Place in knapsack without rotation
                else:
                    for width in range(placement[0], package[1] + placement[0]):
                        for height in range(placement[1], package[2] + placement[1]):
                            knapsack_grid[width][height] = placement_count

                total_value += package[3]

        print(knapsack_grid)
        print("Greedy, " + dimension + ", " + str(time.time() - start_time))
        print("Total value collected:", total_value)

        # Calculate maximum possible value
        max_possible_value = sum(package[3] for package in packages)

        print("Max possible value:", max_possible_value)
        writer.writerow([dimension, time.time() - start_time, total_value, max_possible_value])

if __name__ == '__main__':
    main()