import re


def count_matching_numbers_by_line(line: str):
    winning_numbers_match = re.search(r":([ 0-9]+)\|", line, re.IGNORECASE)
    if winning_numbers_match is None:
        raise RuntimeError("Missing winning numbers")
    winning_numbers = [
        int(item) for item in str(winning_numbers_match.group(1)).split()
    ]

    card_numbers_match = re.search(r"\|([ 0-9]+)$", line, re.IGNORECASE)
    if card_numbers_match is None:
        raise RuntimeError("Missing card numbers")
    card_numbers = [int(item) for item in str(card_numbers_match.group(1)).split()]

    return len(set(winning_numbers) & set(card_numbers))


def part1(input_file_path: str):
    result = 0
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            match_count = count_matching_numbers_by_line(line)
            if match_count:
                result = result + (2 ** (match_count - 1))
    return result


if __name__ == "__main__":
    print(part1("inputs/day4_input.txt"))
