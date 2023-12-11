import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def part1(input_file_path: str):
    valid_game_ids: list[int] = []
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()

            match_game_id = re.search(r"Game (\d+):", line, re.IGNORECASE)
            if match_game_id is None:
                raise RuntimeError("Missing game ID")
            game_id = int(str(match_game_id.group(1)))

            red_draws = re.findall(r"(\d+) red", line)
            if any(int(draw) > RED_MAX for draw in red_draws):
                continue
            green_draws = re.findall(r"(\d+) green", line)
            if any(int(draw) > GREEN_MAX for draw in green_draws):
                continue
            blue_draws = re.findall(r"(\d+) blue", line)
            if any(int(draw) > BLUE_MAX for draw in blue_draws):
                continue

            valid_game_ids.append(game_id)
    return sum(valid_game_ids)


def part2(input_file_path: str):
    result: int = 0
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()

            red_draws = re.findall(r"(\d+) red", line)
            green_draws = re.findall(r"(\d+) green", line)
            blue_draws = re.findall(r"(\d+) blue", line)

            max_red_cubes = max(int(draw) for draw in red_draws)
            max_green_cubes = max(int(draw) for draw in green_draws)
            max_blue_cubes = max(int(draw) for draw in blue_draws)
            power = max_red_cubes * max_green_cubes * max_blue_cubes

            result = result + power
    return result


if __name__ == "__main__":
    print(part1("inputs/day2_input.txt"))
    print(part2("inputs/day2_input.txt"))
