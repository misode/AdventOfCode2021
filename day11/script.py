
with open('day11/in.txt') as f:
	grid = [[int(c) for c in l.rstrip()] for l in f.readlines()]

	p1 = 0
	p2 = 0
	N = len(grid)
	S = 1000

	for step in range(S):
		for x in range(N):
			for y in range(N):
				grid[y][x] += 1

		flashed = set()
		while True:
			running = False
			for x in range(N):
				for y in range(N):
					if grid[y][x] > 9 and (x, y) not in flashed:
						flashed.add((x, y))
						for xo in range(-1, 2):
							for yo in range(-1, 2):
								if 0<=x+xo<N and 0<=y+yo<N and (x+xo, y+yo) not in flashed:
									grid[y+yo][x+xo] += 1
									running = True
			if not running:
				break

		for x in range(N):
			for y in range(N):
				if grid[y][x] > 9:
					grid[y][x] = 0
		if step < 100:
			p1 += len(flashed)
		if p2 == 0 and len(flashed) == N * N:
			p2 = step + 1
			break

	print(p1)
	print(p2)
