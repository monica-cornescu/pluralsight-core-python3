def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


def main():
    banner("Welcome to Earth!")
    banner("Good luck finding the best job for you!", border="*")
    banner(border=".", message="Save the world, make it a better place!!!")
    print(add_spam(["eggs", "salad"]))
    print(add_spam())


if __name__ == '__main__':
    main()
