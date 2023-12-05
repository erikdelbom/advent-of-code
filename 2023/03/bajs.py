import argparse
import math
import re
import time

def solve(input_file: str) -> tuple:
    """Solve AoC 2023 Day Day 3: Gear Ratios"""
    with open(input_file) as f:
        input = [line.strip() for line in f.readlines()]

    symbols: set[tuple] = set()
    gears: set[tuple] = set()
    numbers = []
    for row, line in enumerate(input):
        for m in re.finditer(r"\d+|[^0-9.]", line):
            item = m.group(0)
            if item.isdigit():
                numbers.append(
                    (
                        int(item),
                        set(
                            (c, r)
                            for c in range(m.start(0) - 1, m.end(0) + 1)
                            for r in range(row - 1, row + 2)
                        ),
                    )
                )
            else:
                symbols.add((m.start(0), row))
                if item == "*":
                    gears.add((m.start(0), row))

    sum_parts = sum(number for number, area in numbers if len(symbols & area) > 0)

    sum_ratios = 0
    for gear in gears:
        parts = [number for number, area in numbers if gear in area]
        if len(parts) == 2:
            sum_ratios += math.prod(parts)

    return sum_parts, sum_ratios


if __name__ == "__main__":
    t1 = time.perf_counter()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default="example.txt")
    args = parser.parse_args()

    solution_1, solution_2 = solve(args.filename)

    print(f"Answer 1: {solution_1}")
    print(f"Answer 2: {solution_2}")

    t2 = time.perf_counter()
    print("Execution time: {0:0.4f} seconds".format(t2 - t1))