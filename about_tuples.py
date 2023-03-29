""" practice with tuples """


def minmax(items):
    return min(items), max(items)


def print_minmax(result1, result2):
    print(result1, result2)


def main():
    lower, upper = minmax([102, 17, 11, 19, 4])
    print_minmax(lower, upper)


if __name__ == '__main__':
    main()
