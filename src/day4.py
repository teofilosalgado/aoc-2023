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


def part2(input_file_path: str):
    result = {}
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            card_id_match = re.search(r"Card +(\d+):", line, re.IGNORECASE)
            if card_id_match is None:
                raise RuntimeError("Missing card ID")
            card_id: int = int(card_id_match.group(1))
            match_count = count_matching_numbers_by_line(line)

            if card_id not in result:
                result[card_id] = 1

            for n in range(card_id + 1, card_id + 1 + match_count):
                result[n] = result.get(n, 1) + result[card_id]
    return sum(result.values())


if __name__ == "__main__":
    print(part1("inputs/day4_input.txt"))
    print(part2("inputs/day4_input.txt"))
