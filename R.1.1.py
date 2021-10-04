def is_multiple(n, m):
    return n % m == 0;

if __name__ == '__main__':
    print(is_multiple(10, 4))
    print(is_multiple(3, 2))
    print(is_multiple(3, 1))
    print(is_multiple(3, 3))
    print(is_multiple(10, 2))
    print(is_multiple(10, 3))
