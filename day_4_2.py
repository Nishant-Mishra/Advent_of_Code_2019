#!/usr/bin/python3 -u

n_digs = 6

def puzzle(beg, end):

    c = count_valid_combi(beg, end)

    print("Total Combis: %d" % c)

def count_valid_combi(l, f):

    count = 0
    for num in range(l, f + 1):

        cond1 = False
        cond2 = False
        cond3 = False
        # Check condition 1
        tmp1 = conv(num=num)
        tmp2 = list(tmp1["d"])
        tmp2 = "".join(sorted(tmp2))

        if tmp1["d"] == tmp2:
            cond1 = True

        if cond1:
            c = {}
            for i in range(1, len(tmp1["d"])):
                if tmp1["d"][i - 1] == tmp1["d"][i]:
                    cond2 = True
                    if tmp1["d"][i] in c.keys():
                        c[tmp1["d"][i]] += 1

                    else:
                        c[tmp1["d"][i]] = 1
                # print("%d: %s" % (tmp1["n"], repr(c)))

            for k in c.keys():
                if c[k] == 1:
                    cond3 = True
                    break

        else:
            continue

        count += cond1 & cond2 & cond3
        num += 1
        if cond1 & cond2 & cond3:
            print("Num: %s" % repr(tmp1))

    return count

def conv(num=None):

    global n_digs

    data = {"n": num, "d": str(num)}

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
