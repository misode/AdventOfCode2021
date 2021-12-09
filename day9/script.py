with open('day9/in.txt') as f:
	grid = [l.rstrip() for l in f.readlines()]

	X = len(grid[0])
	Y = len(grid)

	p1 = 0
	p2 = 0
	basins = []
	visited = set()

	def get(x, y):
		if (x, y) in visited:
			return 10
		if x < 0 or x >= X or y < 0 or y >= Y:
			return 10
		return int(grid[y][x])

	def low(x, y):
		n = int(grid[y][x])
		if n == 9:
			return False
		return n <= get(x-1, y) and n <= get(x+1, y) and n <= get(x, y-1) and n <= get(x, y+1)

	def dfs(x, y):
		if (get(x, y) > 9):
			return 0
		if (low(x, y)):
			visited.add((x, y))
			return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
		return 0

	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			n = int(char)
			if (low(x, y)):
				p1 += n+1
				basins.append(dfs(x, y))
				visited.clear()

	basins.sort()
	p2 = basins[-1] * basins[-2] * basins[-3]

	print(p1)
	print(p2)
