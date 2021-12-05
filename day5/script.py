from dataclasses import dataclass
import re

def sign(n):
	return (n > 0) - (n < 0)

@dataclass
class Line:
	x1: int
	y1: int
	x2: int
	y2: int

	def __init__(self, text: str):
		match = re.match('(\d+),(\d+) -> (\d+),(\d+)', text)
		self.x1 = int(match[1])
		self.y1 = int(match[2])
		self.x2 = int(match[3])
		self.y2 = int(match[4])

	def is_straight(self):
		return self.x1 == self.x2 or self.y1 == self.y2

	def __iter__(self):
		x, y = self.x1, self.y1
		yield x, y

		while x != self.x2 or y != self.y2:
			x += sign(self.x2 - self.x1)
			y += sign(self.y2 - self.y1)
			yield x, y

	def __repr__(self):
		return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'


with open('day5/in.txt') as f:
	lines = [Line(line.rstrip()) for line in f.readlines()]

	N = 1000
	grid1 = [[0] * N for _ in range(N)]
	grid2 = [[0] * N for _ in range(N)]

	for line in lines:
		for x, y in line:
			if line.is_straight():
				grid1[x][y] += 1
			grid2[x][y] += 1

	def crossings(grid):
		return sum(sum(1 for point in row if point >= 2) for row in grid)

	print('Part 1:', crossings(grid1))
	print('Part 2:', crossings(grid2))


		