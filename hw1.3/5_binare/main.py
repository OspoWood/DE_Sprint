
def toBinary(tebInt:str)->str:
    b = ''
    n = int(tebInt)
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

def toDeciminal(binare:str)->str:
    number = 0
    len_dat = len(binare)
    for i in range(0, len_dat):
        number += int(binare[i]) * (2 ** (len_dat - i - 1))
    return number


def mult_binary(f:str, s:str)->str:
    return toBinary(str(int(toDeciminal(f))*int(toDeciminal(s))))


def main():
    x1="111"
    x2 = "101"
    print(mult_binary(x1, x2))


if __name__ == '__main__':
    main()