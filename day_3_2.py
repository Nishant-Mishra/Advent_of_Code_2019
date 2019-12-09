#!/usr/bin/python3 -u

import sys

def puzzle(filename):

    with open(filename, "r") as f:
        path1 = f.readline()
        path2 = f.readline()

        path1_list_str = path1.strip("\n").split(",")
        path2_list_str = path2.strip("\n").split(",")

        # print(path1_list)
        # print(path2_list)
        # Get relative coords of path
        path1_list = []
        path2_list = []
        for i in range(0, len(path1_list_str)):
            path1_list.append(get_coord(path1_list_str[i]))

        for i in range(0, len(path2_list_str)):
            path2_list.append(get_coord(path2_list_str[i]))

        # print(path1_list)
        # print(path2_list)

        # Get absolute coords of line segments
        path1 = {"complete": [(0, 0)]}
        for i in range(0, len(path1_list)):
            if i:
                path1["complete"].insert(i + 1, (path1["complete"][i][0] + path1_list[i][0], path1["complete"][i][1] + path1_list[i][1]))

            else:
                path1["complete"].insert(1, path1_list[0])

        path2 = {"complete": [(0, 0)]}
        for i in range(0, len(path2_list)):
            if i:
                path2["complete"].insert(i + 1, (path2["complete"][i][0] + path2_list[i][0], path2["complete"][i][1] + path2_list[i][1]))

            else:
                path2["complete"].insert(1, path2_list[0])

        # Segregate vertical and horizontal lines
        path1["vertical"] = []
        path1["horizontal"] = []
        for i in range(1, len(path1["complete"])):
            # 'x' coord is same
            if path1["complete"][i - 1][0] == path1["complete"][i][0]:
                path1["vertical"].append((path1["complete"][i - 1], path1["complete"][i]))

            elif path1["complete"][i - 1][1] == path1["complete"][i][1]:
                path1["horizontal"].append((path1["complete"][i - 1], path1["complete"][i]))

        path2["vertical"] = []
        path2["horizontal"] = []
        for i in range(1, len(path2["complete"])):
            # 'x' coord is same
            if path2["complete"][i - 1][0] == path2["complete"][i][0]:
                path2["vertical"].append((path2["complete"][i - 1], path2["complete"][i]))

            elif path2["complete"][i - 1][1] == path2["complete"][i][1]:
                path2["horizontal"].append((path2["complete"][i - 1], path2["complete"][i]))

        # print("%s\n" % path1["horizontal"])
        # print("%s\n" % path1["vertical"])
        # print("%s\n" % path2["horizontal"])
        # print("%s\n" % path2["vertical"])

        intersection_points_list = [] #{ "pt" : (), "p1" : (), "p2" : () }
        # Check if horizontal line of one path intersects with vertical line of other abd vice-versa
        for h_seg in path1["horizontal"]:
            for v_seg in path2["vertical"]:
                intersection_point = check_intersection(h_seg, v_seg)
                if intersection_point:
                    intersection_points_list.append({ "pt": intersection_point,
                                                      "p1": h_seg,
                                                      "p2": v_seg
                                                      })

        for h_seg in path2["horizontal"]:
            for v_seg in path1["vertical"]:
                intersection_point = check_intersection(h_seg, v_seg)
                if intersection_point:
                    intersection_points_list.append({ "pt": intersection_point,
                                                      "p1": v_seg,
                                                      "p2": h_seg
                                                      })

        # print(intersection_points_list)

        # print(path1["complete"])
        p1_len = {}
        for point in intersection_points_list:
            p1_len[point["pt"]] = 0
            for i in range(1, len(path1["complete"])):
                p1_len[point["pt"]] += get_length(path1["complete"][i], path1["complete"][i - 1])
                print("%s :: [ %s - %s => %s ]" % (point["pt"], path1["complete"][i], path1["complete"][i - 1], p1_len[point["pt"]]))
                if path1["complete"][i] == point["p1"][0]:
                    break
            p1_len[point["pt"]] += get_length(point["pt"], point["p1"][0])
            print("%s :: [ %s - %s => %s ]" % (point["pt"], point["pt"], point["p1"][0], p1_len[point["pt"]]))
            print("\n")

        p2_len = {}
        for point in intersection_points_list:
            p2_len[point["pt"]] = 0
            for i in range(1, len(path2["complete"])):
                p2_len[point["pt"]] += get_length(path2["complete"][i], path2["complete"][i - 1])
                if path2["complete"][i] == point["p2"][0]:
                    break

            p2_len[point["pt"]] += get_length(point["pt"], point["p2"][0])

        print(p1_len)
        print(p2_len)

        min = 0
        for point in intersection_points_list:
            sum = p1_len[point["pt"]] + p2_len[point["pt"]]
            print("%s: %d" % (point["pt"], sum))
            if min == 0:
                min = sum

            elif min > sum:
                min = sum

        print(min)

def get_coord(cmd):

    if cmd[0] == "R":
        return (int(cmd[1:]), 0)

    elif cmd[0] == "L":
        return (-int(cmd[1:]), 0)

    elif cmd[0] == "U":
        return (0, int(cmd[1:]))

    elif cmd[0] == "D":
        return (0, -int(cmd[1:]))

def check_intersection(horiz, vert):

    x = vert[0][0]
    y1 = vert[0][1]
    y2 = vert[1][1]

    w = horiz[0][1]
    z1 = horiz[0][0]
    z2 = horiz[1][0]

    to_return = None
    if  (z1 < z2 and y1 < y2 and z1 <= x <= z2 and y1 <= w <= y2) or\
        (z1 > z2 and y1 < y2 and z1 >= x >= z2 and y1 <= w <= y2) or\
        (z1 < z2 and y1 > y2 and z1 <= x <= z2 and y1 >= w >= y2) or\
        (z1 > z2 and y1 > y2 and z1 >= x >= z2 and y1 >= w >= y2) :
        to_return = (x, w)

    # if to_return:
    #     print("<< %s :: %s >> ==  %s" % (horiz, vert, (x,w)))

    return to_return

def get_length(p1, p2):

    return abs(abs(p2[1]) - abs(p1[1])) + abs(abs(p2[0]) - abs(p1[0]))


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

    puzzle("input_day_3_1.txt")
    # test()

def test():

    p = get_all_points_on_path((123, 67), (123, 15))
    p = get_all_points_on_path((-123, 67), (123, 67))

    print(p)

if __name__ == "__main__":
    main()
