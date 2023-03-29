""" learn and practice with ranges and enumerations """

t = [5, 22, 437, 59, 8]


if __name__ == '__main__':
    for p in enumerate(t):
        print(p)

    for i, v in enumerate(t):
        print(f"i = {i}, v = {v}")