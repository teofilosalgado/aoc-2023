import re
from typing import List


def build_almanac_from_seeds(line: str, categories: int) -> List[List[int]]:
    seed_ids_row = [int(item) for item in next(reversed(line.split(":"))).split()]
    result = [
        seed_ids_row,
        *[[0 for _ in range(len(seed_ids_row))] for _ in range(categories)],
    ]
    return result


def part1(input_file_path: str):
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        data = input_file.read()

    seeds_match = re.search(r"seeds:([ 0-9]+)$", data, re.MULTILINE)
    if seeds_match is None:
        raise RuntimeError("Seeds definition not found")
    seeds: str = seeds_match.group(1)
    almanac = build_almanac_from_seeds(seeds, 7)

    stages = re.findall(r"^[- a-z]+map:\n([ 0-9\n]+)", data, re.MULTILINE)
    for index, stage in enumerate(stages):
        source_stage_index = index
        destination_stage_index = index + 1
        ranges = [
            [int(value) for value in item.split()] for item in stage.split("\n") if item
        ]
        for range in ranges:
            destination_range_start, source_range_start, range_length = range
            for source_item_column, source_item_id in enumerate(
                almanac[source_stage_index]
            ):
                if (
                    source_item_id >= source_range_start
                    and source_item_id < source_range_start + range_length
                ):
                    destination_item_id = destination_range_start + (
                        source_item_id - source_range_start
                    )
                    almanac[destination_stage_index][
                        source_item_column
                    ] = destination_item_id
        for index, item in enumerate(almanac[destination_stage_index]):
            if item == 0:
                almanac[destination_stage_index][index] = almanac[source_stage_index][
                    index
                ]
    return min(almanac[len(almanac) - 1])


if __name__ == "__main__":
    print(part1("inputs/day5_input.txt"))
