def main():
    words = input("Greeting: ").title()
    print('$' + value(words))


def value(greeting):
    greeting = greeting.title()
    if greeting.find("Hello") == 0:
        return 0
    elif greeting.find("H") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
