def is_string_palindrom(input_string: str) -> bool:
    input_string = clear_string(input_string)
    length = len(input_string)
    count = 0
    start_index = 0
    end_position = length - 1
    while count < length / 2:
        if input_string[start_index] != input_string[end_position]:
            return False
        start_index += 1
        end_position -= 1
        count += 1
    return True


def clear_string(s: str) -> str:
    return s.replace(" ", "")


def main():
    print(is_string_palindrom("taco cat"))
    print(is_string_palindrom("rotator"))
    print(is_string_palindrom("black cat"))


if __name__ == '__main__':
    main()
