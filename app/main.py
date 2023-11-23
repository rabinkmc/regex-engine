import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_digit(line):
    return any(char.isdigit() for char in line)


def match_words(line):
    for char in line:
        if ord(char) >= ord("0") and ord(char) <= ord("9"):
            return True
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            return True
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True
        if char == "_":
            return True
    return False


def match_pattern(line: str, pattern: str):
    if pattern == "\\w":
        return match_words(line)
    if pattern == "\\d":
        return match_digit(line)
    if len(pattern) == 1:
        return pattern in line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
