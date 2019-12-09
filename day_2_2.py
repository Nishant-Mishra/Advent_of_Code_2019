#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    idx_opcode = 0

    with open(filename, "r") as f:
        line = f.readline()

        if len(line) > 0:
            intcode_str = line.split(",")

            for i in range(0, 99):
                for j in range(1, 99):
                    intcode = [int(x) for x in intcode_str]

                    idx_opcode = 0

                    intcode[1] = i
                    intcode[2] = j

                    while idx_opcode < len(intcode):
                        opcode = intcode[idx_opcode]

                        if opcode == 99:
                            break

                        elif opcode == 1:
                            try:
                                val = intcode[intcode[idx_opcode + 1]] + \
                                      intcode[intcode[idx_opcode + 2]]
                            except IndexError as e:
                                print("ERROR: %s" % e, file=sys.stderr)

                            else:
                                intcode[intcode[idx_opcode + 3]] = val

                        elif opcode == 2:
                            try:
                                val = intcode[intcode[idx_opcode + 1]] * intcode[intcode[idx_opcode + 2]]
                            except IndexError as e:
                                print("ERROR: %s" % e, file=sys.stderr)

                            else:
                                intcode[intcode[idx_opcode + 3]] = val

                        else:
                            print("ERROR: Unknown Opcode %d found" % opcode)

                        idx_opcode += 4

                    if intcode[0] == 19690720:
                        break

                if intcode[0] == 19690720:
                    break

            print(100 * intcode[1] + intcode[2])


def main():

        puzzle("input_day_2_1.txt")


if __name__ == "__main__":
    main()
