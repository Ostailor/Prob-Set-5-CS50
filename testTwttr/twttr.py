def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(s="TRUE"):
    omit = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = ''
    for _ in s:
        if _ in omit:
            continue
        else:
            string = string + _
    return f'{string}'


if __name__ == "__main__":
    main()
