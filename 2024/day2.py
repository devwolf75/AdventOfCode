reports = []


def main():
    with open("./inputs/data_bear.txt", "r", encoding="utf-8") as f:
        # Part 1
        for line in f:
            levels = list(map(int, line.split(" ")))
            safe = check_level_rules(levels)

            # Part 2 - check if removing one or more levels makes it safe.
            # Brute forcing cause I'm not a pacient man.
            # Comment for only part one.
            if not safe:
                for i, level in enumerate(levels):
                    levels2 = levels.copy()
                    del levels2[i]
                    safe2 = check_level_rules(levels2)
                    if safe2:
                        safe = True
                        break
            # End of part 2

            reports.append(1 if safe else 0)


def check_level_rules(levels):
    direction = "+" if levels[0] < levels[1] else "-"

    for i in range(len(levels) - 1):
        difference = abs(levels[i] - levels[i + 1])
        if (
            (direction == "+" and levels[i] > levels[i + 1])
            or (direction == "-" and levels[i] < levels[i + 1])
            or (levels[i] == levels[i + 1])
            or (difference < 1 or difference > 3)
        ):
            return False
    return True


if __name__ == "__main__":
    main()
    print(sum(reports))
