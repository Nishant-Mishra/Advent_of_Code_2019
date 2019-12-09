#!/usr/bin/python3 -u

import sys

n_digs = 7

def puzzle(beg, end):

    c = count_valid_combi(beg, end)

    print("Total Combis: %d" % c)

def count_valid_combi(l, f):

    count = 0
    for num in range(l, f + 1):

        cond1 = False
        cond2 = False
        # Check condition 1
        tmp1 = conv(num=num)
        tmp2 = list(tmp1["d"])
        tmp2.sort()

        if tmp1["d"] == tmp2:
            cond1 = True
            for i in range(1, len(tmp1["d"])):
                if tmp1["d"][i - 1] == tmp1["d"][i]:
                    cond2 = True

        else:
            continue
        count += cond1 & cond2
        num += 1
        if cond1 & cond2:
            print("Num: %s" % repr(tmp1))

    return count

def conv(num=None, list_dig=None):

    global n_digs

    if not list_dig and num:
        data = {"n": num}

        l = []
        for i in range(0, n_digs):
            l.insert(i, int(num%10))
            i += 1
            num = int(num/10)

        l.reverse()
        data["d"] = l

    elif not num and list_dig:
        data = {"d": list_dig}

        n = 0
        for d in list_dig:
            n = n * 10 + d

        data["n"] = n

    else:
        data = {"n": 0, "d": [0]}

    return data

def main():

    puzzle(206938, 679128)

def test():

    global n_digs
    count_valid_combi(206938, 679128)

    # print(conv(num=1912))
    # print(conv(list_dig=[2,3,5,6]))
    # print(conv())


if __name__ == "__main__":
    main()
