import csv

from time import time
from naive_pattern_search import naive_pattern_search
from rabin_karp_pattern_matching import rabin_karp_pattern_matching


def main():
    sample_data = []
    pattern = ['ABC', 'B??', 'C??']
    f = open('results2.csv', 'w')
    header = ['N', 'naive', 'fabin_f', 'rabin_hash']
    writer = csv.writer(f, dialect='excel')
    writer.writerow(header)
    print('Dla 1000:')
    sample_data = [char for char in open('1000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()

    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([1000, naive_end - naive_start, rabin_end - naive_end, hash_time])
    print('Dla 2000:')
    sample_data = [char for char in open('2000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()

    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([2000, naive_end - naive_start, rabin_end - naive_end, hash_time])
    print('Dla 3000:')
    sample_data = [char for char in open('3000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()

    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([3000, naive_end - naive_start, rabin_end - naive_end, hash_time])
    print('Dla 4000:')
    sample_data = [char for char in open('4000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()
    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([4000, naive_end - naive_start, rabin_end - naive_end, hash_time])
    print('Dla 5000:')
    sample_data = [char for char in open('5000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()
    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([5000, naive_end - naive_start, rabin_end - naive_end, hash_time])
    print('Dla 8000:')
    sample_data = [char for char in open('8000_pattern.txt', 'r').read().splitlines()]
    naive_start = time()
    naive_pattern_search(sample_data, pattern)
    naive_end = time()
    hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
    rabin_end = time()
    writer.writerow([8000, naive_end - naive_start, rabin_end - naive_end, hash_time])



if __name__ == '__main__':
    main()
