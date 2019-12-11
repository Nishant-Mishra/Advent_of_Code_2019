#!/usr/bin/python3 -u

import json

def puzzle(filename):

    d = {}
    with open(filename, "r") as f:
        while True:
            line = f.readline()

            if not line:
                break

            else:
                node = line.strip("\n").split(")")

                if node[0] in d:
                    d[node[0]].append(node[1])
                else:
                    d[node[0]] = [node[1]]

    # print(d)
    sun = ""
    v_len = len(d.values())
    for k in d.keys():
        i = 0
        for v in d.values():
            if k in v:
                break
            else:
                i += 1

        if i == v_len:
            sun = k
            break

    # print(sun)

    d2 = {}
    stack = []
    keys = list(d.keys())
    # print(keys)
    planet = sun
    d2[planet] = 0
    while True:
        if planet in keys:
            # print(d[planet])
            for i in d[planet]:
                d2[i] = d2[planet] + 1
                stack.append(i)

        if stack:
            planet = stack.pop()

        else:
            break

    # print(d2)

    sum = 0
    for k in d2.keys():
        sum += d2[k]

    print(sum)


def main():

    puzzle("input_day_6_1.txt")


if __name__ == "__main__":
    main()
