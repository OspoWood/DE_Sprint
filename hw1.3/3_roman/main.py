def to_roman(num: int) -> str:
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M CM D CD C XC L XL X IX V IV I'.split()):
        result += num // arabic * roman
        num %= arabic
    return result


def main():
    x1 = 3
    print(to_roman(x1))
    x2 = 9
    print(to_roman(x2))
    x3 = 1945
    print(to_roman(x3))


if __name__ == '__main__':
    main()
