def consecutive_zeros(string):
    count = 0
    highestcount = 0

    for x in string:
        if x == "0":
            count += 1
        elif x != "0": count = 0
        highestcount = max(highestcount, count)
    print(highestcount)
consecutive_zeros("10011010000000110")

