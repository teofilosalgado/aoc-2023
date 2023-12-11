import re
from functools import reduce


def get_neighbors(max_y: int, max_x: int, coordinates: list[tuple[int, int]]):
    results: set[tuple[int, int]] = set([])
    for coordinate in coordinates:
        y = coordinate[0]
        x = coordinate[1]
        neighbor_coordinates = [
            (y, x - 1),
            (y, x + 1),
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
        ]
        filtered_coordinates = [
            neighbor_coordinate
            for neighbor_coordinate in neighbor_coordinates
            if neighbor_coordinate[0] >= 0
            and neighbor_coordinate[0] < max_y
            and neighbor_coordinate[1] >= 0
            and neighbor_coordinate[1] < max_x
        ]
        results = results.union(filtered_coordinates)
    return results


def part1(input_file_path: str):
    data: list[str] = []
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            data.append(line.rstrip())

    result: int = 0
    for index, line in enumerate(data):
        candidates = re.finditer(r"(\d+)", line)
        for candidate in candidates:
            candidate_value = int(candidate.group(1))
            candidate_coordinates = [
                (index, item) for item in list(range(*candidate.span()))
            ]
            candidate_neighbors = [
                data[item[0]][item[1]]
                for item in get_neighbors(len(data), len(line), candidate_coordinates)
            ]
            is_candidate_valid = any(
                bool(re.search(r"[^\d\.\n]", candidate_neighbor))
                for candidate_neighbor in candidate_neighbors
            )
            if is_candidate_valid:
                result = result + candidate_value
    return result


def part2(input_file_path: str):
    data: list[str] = []
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            data.append(line.rstrip())

    result: int = 0

    tokens: list[set[tuple[int, int]]] = []
    for index, line in enumerate(data):
        asterisks = re.finditer(r"(\*)", line)
        for asterisk in asterisks:
            token_coordinates = [
                (index, item) for item in list(range(*asterisk.span()))
            ]
            token_neighbors = get_neighbors(len(data), len(line), token_coordinates)
            tokens.append(token_neighbors)

    gears: list[tuple[int, set[tuple[int, int]]]] = []
    for index, line in enumerate(data):
        digits = re.finditer(r"(\d+)", line)
        for digit in digits:
            digit_value = int(digit.group(1))
            cdigit_coordinates = set(
                [(index, item) for item in list(range(*digit.span()))]
            )
            gears.append((digit_value, cdigit_coordinates))

    for token in tokens:
        parts = [gear for gear in gears if token.intersection(gear[1])]
        if len(parts) > 1:
            ratio = reduce(lambda x, y: x * y, [part[0] for part in parts])
            result = result + ratio

    return result


if __name__ == "__main__":
    print(part1("inputs/day3_input.txt"))
    print(part2("inputs/day3_input.txt"))
