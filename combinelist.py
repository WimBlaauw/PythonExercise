
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

lenlist1 = len(list1)
lenlist2 = len(list2)

newlist = ""
index =0

if lenlist1 == lenlist2:
    for x in range(lenlist1):
        newlist += list1[index]
        newlist += list2[index]
        newlist += " "
        index += 1
    print(newlist)
else: print("lists do not have the same lenght.")
