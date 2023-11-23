import sys


def match_digit(char: str):
    return ord("0") <= ord(char) <= ord("9")


def match_alphabets(char: str):
    is_upper = ord("A") <= ord(char) <= ord("Z")
    is_lower = ord("a") <= ord(char) <= ord("z")
    return is_upper or is_lower


def match_alphanum(char: str):
    return match_alphabets(char) or match_digit(char) or char == "_"


def match_pcg(group: str, char: str):
    return char in group


def match_ncg(group: str, char: str):
    return char not in group


def is_ncgp(pattern):
    return len(pattern) >= 4 and pattern[0:2] == "[^" and pattern[-1] == "]"


def is_pcgp(pattern):
    return len(pattern) >= 3 and pattern[0] == "[" and pattern[-1] == "]"


def is_alphap(pattern):
    return pattern == "\\w"


def is_digitp(pattern):
    return pattern == "\\d"


def match_character(pattern: str, char: str):
    if is_ncgp(pattern):
        return match_ncg(pattern, char)
    if is_pcgp(pattern):
        return match_pcg(pattern, char)
    if is_alphap(pattern):
        return match_alphanum(char)
    if is_digitp(pattern):
        return match_digit(char)
    return pattern == char


def parse(regex: str):
    j = 0
    pattern = []
    while j < len(regex):
        if regex[j : j + 2] == "\\d":
            j += 2
            pattern.append("\\d")
        elif regex[j : j + 2] == "\\w":
            j += 2
            pattern.append("\\w")
        elif regex[j : j + 2] == "[^" and regex.find("]") != -1:
            end = regex.find("]") + 1
            pattern.append(regex[j:end])
            j = end
        elif regex[j : j + 1] == "[" and regex.find("]") != -1:
            end = regex.find("]") + 1
            pattern.append(regex[j:end])
            j = end
        else:
            pattern.append(regex[j])
            j += 1
    return pattern


def match_pattern(text: str, regex: str):
    i = 0
    start_flag = False
    end_flag = False
    if regex[0] == "^":
        regex = regex[1:]
        start_flag = True

    if regex[-1] == "$":
        regex = regex[0:-1]
        end_flag = True

    pattern = parse(regex)
    while i < len(text):
        j = 0
        while (
            j < len(pattern) and i < len(text) and match_character(pattern[j], text[i])
        ):
            i += 1
            j += 1
        if j == len(pattern) and (not end_flag or (i + 1 == len(text))):
            return True

        if start_flag:
            return False

        i = i + 1

    return False


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
