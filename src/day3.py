import re


def get_neighbors(data: list[str], coordinates: list[tuple[int, int]]):
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
            and neighbor_coordinate[0] < len(data)
            and neighbor_coordinate[1] >= 0
            and neighbor_coordinate[1] < len(data[0])
        ]
        results = results.union(filtered_coordinates)
    return [data[item[0]][item[1]] for item in results]


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
            candidate_neighbors = get_neighbors(data, candidate_coordinates)
            is_candidate_valid = any(
                bool(re.search(r"[^\d\.\n]", candidate_neighbor))
                for candidate_neighbor in candidate_neighbors
            )
            if is_candidate_valid:
                result = result + candidate_value
    return result


if __name__ == "__main__":
    print(part1("inputs/day3_input.txt"))
