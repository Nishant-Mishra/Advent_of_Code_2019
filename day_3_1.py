#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    with open(filename, "r") as f:
        path1 = f.readline()
        path2 = f.readline()

        path1_list = path1.strip("\n").split(",")
        path2_list = path2.strip("\n").split(",")

        # print(path1_list)
        # print(path2_list)

        for i in range(0, len(path1_list)):
            path1_list[i] = get_coord(path1_list[i])

        for i in range(0, len(path2_list)):
            path2_list[i] = get_coord(path2_list[i])

        # print(path1_list)
        # print(path2_list)

        path1 = []
        for i in range(0, len(path1_list)):
            if i:
                path1.insert(i, (path1[i - 1][0] + path1_list[i][0], path1[i - 1][1] + path1_list[i][1]))

            else:
                path1.insert(0, path1_list[0])

        path2 = []
        for i in range(0, len(path2_list)):
            if i:
                path2.insert(i, (path2[i - 1][0] + path2_list[i][0], path2[i - 1][1] + path2_list[i][1]))

            else:
                path2.insert(0, path2_list[0])

        path1_points = []
        for i in range(1, len(path1)):
            path1_points.extend(get_all_points_on_path(path1[i - 1], path1[i]))

        path2_points = []
        for i in range(1, len(path2)):
            path2_points.extend(get_all_points_on_path(path2[i - 1], path2[i]))

        print(len(path1_points))
        print(len(path2_points))

        intersection_points = []
        for point in path2_points:
            try:
                path1_points.index(point)
            except ValueError:
                pass
            else:
                intersection_points.append(point)

        print(intersection_points)

        dist = abs(intersection_points[0][0]) + abs(intersection_points[0][1])
        for point in intersection_points[1:]:
            if dist > (abs(point[0]) + abs(point[1])):
                dist = abs(point[0]) + abs(point[1])

        print("Shortest Dist: %d" % dist)

def get_coord(cmd):

    if cmd[0] == "R":
        return (int(cmd[1:]), 0)

    elif cmd[0] == "L":
        return (-int(cmd[1:]), 0)

    elif cmd[0] == "U":
        return (0, int(cmd[1:]))

    elif cmd[0] == "D":
        return (0, -int(cmd[1:]))

def get_all_points_on_path(c1, c2):

    coord_list = []
    if c1[0] == c2[0]:
        if c1[1] < c2[1]:
            for i in range(c1[1], c2[1] + 1):
                coord_list.append((c1[0], i))
        else:
            for i in range(c2[1], c1[1] + 1):
                coord_list.append((c1[0], i))

            # coord_list.reverse()

    elif c1[1] == c2[1]:
        if c1[0] < c2[0]:
            for i in range(c1[0], c2[0] + 1):
                coord_list.append((i, c1[1]))

        else:
            for i in range(c2[0], c1[0] + 1):
                coord_list.append((i, c1[1]))

            # coord_list.reverse()

    return coord_list


def main():

    puzzle("input_day_3_1_sample.txt")
    # test()

def test():

    p = get_all_points_on_path((123, 67), (123, 15))
    p = get_all_points_on_path((-123, 67), (123, 67))

    print(p)

if __name__ == "__main__":
    main()
