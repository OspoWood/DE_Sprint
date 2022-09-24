def is_mirred(inputString: str) -> bool:
    list = [*inputString]
    if len(inputString) % 2 != 0:
        return False
    return all(list.count(start) == list.count(end) for start, end in zip("[({", "])}"))


def main():
    f = "[{}({})]"
    print(is_mirred(f))
    s = "{]"
    print(is_mirred(s))
    t = '{'
    print(is_mirred(t))


if __name__ == '__main__':
    main()
