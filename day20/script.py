
fp = open('day20/in.txt')
A = [c == '#' for c in fp.readline().rstrip()]
fp.readline()
lines = [line.rstrip() for line in fp.readlines()]

R = len(lines[0])
C = len(lines)

S = set()
for x in range(R):
	for y in range(C):
		if lines[y][x] == '#':
			S.add((x, y))

NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

N = 50

for s in range(N):
	T = set()
	for x in range(-2*N, R + 2*N):
		for y in range(-2*N, C + 2*N):
			n = sum(2**(8-i) for i, (dx, dy) in enumerate(NEIGHBORS) if (x+dx, y+dy) in S)
			if A[n]:
				T.add((x, y))
	S = T
	if s + 1 in (2, 50):
		print(len([1 for (x, y) in S if -N<=x<R+N and -N<=y<C+N]))
