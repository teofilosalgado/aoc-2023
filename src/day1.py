def main(input_file_path: str):
    result: int = 0
    with open(input_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            first_number = next(x for x in line if x.isdigit())
            last_number = next(x for x in reversed(line) if x.isdigit())
            current = int(f"{first_number}{last_number}")
            result = result + current
    return result


if __name__ == "__main__":
    print(main("inputs/day1_input1.txt"))
