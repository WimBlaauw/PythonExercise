from heapq import merge


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 18, 20, 24, 28]
l3 = []
l4 = []
for x in l1:
    if x%2 == 0:
        l3.append(x)
print(l3+ l2[0::2])

