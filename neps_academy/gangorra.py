p1, c1, p2, c2 = input().split(" ")
l1 = int(p1) * int(c1)
l2 = int(p2) * int(c2)

if l1 == l2:
    print(0)
elif l1 > l2:
    print(-1)
else: print(1)