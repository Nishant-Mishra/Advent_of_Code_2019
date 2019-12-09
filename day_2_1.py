#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    idx_opcode = 0

    with open(filename, "r") as f:
        while True:
            line = f.readline()

            if not line:
                break

            if len(line) > 0:
                intcode_str = line.split(",")

                intcode = [int(x) for x in intcode_str]

                intcode[1] = 12
                intcode[2] = 2

                while idx_opcode < len(intcode):
                    opcode = intcode[idx_opcode]

                    # print("INFO: Found opcode %d at %d, Operation Set: [%d, %d, %d, %d]" % (opcode, idx_opcode,
                    #                                                                         intcode[idx_opcode],
                    #                                                                         intcode[idx_opcode + 1],
                    #                                                                         intcode[idx_opcode + 2],
                    #                                                                         intcode[idx_opcode + 3]))
                    if opcode == 99:
                        # print("INFO: Opcode 99 found at %d" % idx_opcode)
                        break

                    elif opcode == 1:
                        try:
                            # print("INFO: Getting op1 ([%d] = %d) and op2 ([%d] = %d) for opcode 1" %
                            #       (intcode[idx_opcode + 1], intcode[intcode[idx_opcode + 1]], intcode[idx_opcode + 2],
                            #        intcode[intcode[idx_opcode + 2]]))
                            val = intcode[intcode[idx_opcode + 1]] + \
                                  intcode[intcode[idx_opcode + 2]]
                        except IndexError as e:
                            print("ERROR: %s" % e, file=sys.stderr)

                        else:
                            intcode[intcode[idx_opcode + 3]] = val

                    elif opcode == 2:
                        try:
                            # print("INFO: Getting op1 ([%d] = %d) and op2 ([%d] = %d) for opcode 2" %
                            #       (intcode[idx_opcode + 1], intcode[intcode[idx_opcode + 1]], intcode[idx_opcode + 2],
                            #        intcode[intcode[idx_opcode + 2]]))
                            val = intcode[intcode[idx_opcode + 1]] * intcode[intcode[idx_opcode + 2]]
                        except IndexError as e:
                            print("ERROR: %s" % e, file=sys.stderr)

                        else:
                            intcode[intcode[idx_opcode + 3]] = val

                    else:
                        print("ERROR: Unknown Opcode %d found" % opcode)

                    idx_opcode += 4

                print("\n\nINFO: Program Halted, with [0] = %d" % intcode[0])

def main():

        puzzle("input_day_2_1.txt")


if __name__ == "__main__":
    main()
