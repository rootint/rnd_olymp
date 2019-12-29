n = int(input())
a = list(map(int, input().split()))
b = []
res = 0
k = 0
i = 0
mind = 0
while mind + 1 <= n:
    maxx = 0
    mind = 0
    for j in range(i, len(a)):
        if a[j] > maxx:
            maxx = a[j]
            mind = j
    print(maxx, mind)
    if mind + 1 >= n:
        res += (maxx * (n - k))
        break
    else:
        res += maxx * (mind + 1 - i)
        k += mind
    print(i, res)
    i = mind + 1
print(res)
