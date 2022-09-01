def main():
    while True:
        try:
            fuel = input("Fraction: ")
            amount = convert(fuel)
            if amount > 100:
                pass
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(amount), end='')


def convert(fraction):
    x = fraction[0: fraction.find("/")]
    y = fraction[fraction.find("/") + 1:]
    x = int(x)
    y = int(y)
    return round(float(x / y) * 100)


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
