#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    lineno = 0
    total_fuel = 0
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            lineno += 1

            if not line:
                break

            if len(line) > 0:
                try:
                    mass = int(line)
                except (TypeError, ValueError) as e:
                    print("ERROR: Invalid value %s in file at line %d" % (repr(line), lineno), file=sys.stderr)
                    continue
                fuel = int(mass / 3) - 2
                print("INFO: For mass %d, the fuel needed is %d" % (mass, fuel), file=sys.stderr)

                total_fuel += fuel

    print(total_fuel)


def main():

        puzzle("input_day_1_1.txt")


if __name__ == "__main__":
    main()
