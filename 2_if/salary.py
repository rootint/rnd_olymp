x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
def get_distance():
	return ((x1 + x2) ** 2 + (y1 + y2) ** 2) ** 0.5
dist = get_distance()
print(dist)
if r1 + r2 >= dist and r1 + dist > r2 and r2 + dist > r1:
	print('YES')
else:
	print('NO')