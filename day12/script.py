from collections import defaultdict

with open('day12/in.txt') as f:
	edges = [tuple(l.rstrip().split('-')) for l in f.readlines()]

	p1 = 0
	p2 = 0

	G = defaultdict(lambda: set())
	for e in edges:
		G[e[0]].add(e[1])
		G[e[1]].add(e[0])

	def solve(n, twice):
		global p1
		global p2
		for a in G[n]:
			if a == 'end':
				p1 += 0 if twice else 1
				p2 += 1
			elif a == 'start':
				pass
			elif a not in visited or 'A' <= a[0] <= 'Z':
				visited.append(a)
				solve(a, twice)
				visited.pop()
			elif not twice and visited.count(a) < 2:
				visited.append(a)
				solve(a, True)
				visited.pop()

	visited = ['start']
	solve('start', False)

	print(p1)
	print(p2)
