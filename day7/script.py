with open('day7/in.txt') as f:
	crabs = [int(e) for e in f.readline().rstrip().split(',')]

	N = max(crabs)+1
	C = [crabs.count(i) for i in range(N)]
	F = [sum(j+1 for j in range(i)) for i in range(N)]

	def solve(cost):
		return min(
			sum(
				cost(abs(i - n)) * c
				for i, c in enumerate(C)
			)
			for n in range(N)
		)

	print('Part 1:', solve(lambda d: d))
	print('Part 2:', solve(lambda d: F[d]))
