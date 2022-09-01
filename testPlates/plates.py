def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    omit = [".", " ", "?", "!"]
    num0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # length greater than 6 or less than 2
    if len(s) > 6 or len(s) < 2:
        return False

    # plate has punctuation, space, or period
    for c in s:
        if c in omit:
            return False

    # plates first two indexes are numbers
    if s[0] in num0 or s[1] in num0:
        return False

    for c in range(len(s)):
        if s[c].isnumeric():
            if int(s[c]) == 0:
                return False
            elif s[c] in num:
                break

    for c in range(len(s)):
        if s[c] in num and s[-1].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
