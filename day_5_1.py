#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    idx_opcode = 0
    output = 0

    with open(filename, "r") as f:
        while True:
            line = f.readline()

            if not line:
                break

            if len(line) > 0:
                intcode_str = line.split(",")

                intcode = [int(x) for x in intcode_str]

                # Initialize with input = 1
                if intcode[0] == 3:
                    intcode[intcode[1]] = 1

                idx_opcode = 2
                param_mode = [0,0,0]
                while idx_opcode < len(intcode):

                    opcode = int(intcode[idx_opcode] % 100)
                    modes = int(intcode[idx_opcode] / 100)

                    param_mode[0] = modes % 10
                    modes = int(modes / 10)
                    param_mode[1] = modes % 10
                    modes = int(modes / 10)
                    param_mode[2] = modes % 10

                    if param_mode[2] == 1:
                        print("ERROR: Instruction Output Mode is Immediate!!")

                    # First Param
                    idx_opcode += 1

                    op1 = 0
                    op2 = 0
                    if opcode == 1 or opcode == 2:
                        try:
                            op1 = 0
                            if param_mode[0] == 0:
                                op1 = intcode[intcode[idx_opcode]]
                            elif param_mode[0] == 1:
                                op1 = intcode[idx_opcode]

                            # Second Param
                            idx_opcode += 1

                            op2 = 0
                            if param_mode[1] == 0:
                                op2 = intcode[intcode[idx_opcode]]
                            elif param_mode[1] == 1:
                                op2 = intcode[idx_opcode]

                            # Third Param
                            idx_opcode += 1

                        except IndexError as e:
                            print("ERROR: %s" % e, file=sys.stderr)

                    if opcode == 1:
                        intcode[intcode[idx_opcode]] = op1 + op2

                        # Next Opcode
                        idx_opcode += 1

                    elif opcode == 2:
                        intcode[intcode[idx_opcode]] = op1 * op2

                        # Next Opcode
                        idx_opcode += 1

                    elif opcode == 3:
                        print("ERROR: Found opcode '3' in mid of Input!!")

                        # Next Opcode
                        idx_opcode += 1

                    elif opcode == 4:
                        try:
                            if param_mode[0] == 0:
                                output = intcode[intcode[idx_opcode]]
                            elif param_mode[0] == 1:
                                output = intcode[idx_opcode]
                        except IndexError as e:
                            print("ERROR: %s" % e, file=sys.stderr)

                        # Next Opcode
                        idx_opcode += 1

                    elif opcode == 99:
                        # print("INFO: Opcode 99 found at %d" % idx_opcode)
                        break

                    else:
                        print("ERROR: Unknown Opcode %d found" % opcode)

                print("\n\nINFO: Program Halted, with Output = %d\n\n" % output)

def main():

        puzzle("input_day_5_1.txt")


if __name__ == "__main__":
    main()
