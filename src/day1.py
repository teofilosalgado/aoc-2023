lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def find_number(line: str, is_reversed: bool = False):
    buffer = ""
    for character in line:
        if is_reversed:
            buffer = character + buffer
        else:
            buffer = buffer + character
        if character.isdigit():
            return character
        if match := next((key for key in lookup.keys() if key in buffer), None):
            return buffer.replace(buffer, lookup[match])


def main(input_file_path: str):
    result: int = 0
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.read().splitlines():
            first_number = find_number(line)
            last_number = find_number(line[::-1], True)
            current = int(f"{first_number}{last_number}")
            result = result + current
    return result


if __name__ == "__main__":
    print(main("inputs/day1_input1.txt"))
    print(main("inputs/day1_input2.txt"))
