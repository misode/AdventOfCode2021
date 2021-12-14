from collections import Counter, defaultdict

with open('day14/in.txt') as f:
	initial = list(f.readline().rstrip())
	f.readline()
	rules = dict([tuple(l.rstrip().split(' -> ')) for l in f.readlines()])

	Q = Counter()
	for a, b in zip(initial, initial[1:]):
		Q[a, b] += 1

	for s in range(40):
		R = Counter()
		for a, b in Q:
			mid = rules[a + b]
			if mid:
				R[a, mid] += Q[a, b]
				R[mid, b] += Q[a, b]
		Q = R
		if s+1 in [10, 40]:
			C = Counter()
			for a, b in Q:
				C[a] += Q[a, b]
			C[initial[-1]] += 1
			print(max(C.values()) - min(C.values()))
