C = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

S = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

A = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

with open('day10/in.txt') as f:
	lines = [l.rstrip() for l in f.readlines()]

	p1 = 0
	p2 = []

	for line in lines:
		stack = []
		corrupt = False
		for char in line:
			if char in C:
				stack.append(C[char])
			else:
				expect = stack.pop()
				if char != expect:
					p1 += S[char]
					corrupt = True
					break
		if not corrupt and stack:
			score = 0
			for a in reversed(stack):
				score *= 5
				score += A[a]
			p2.append(score)

	p2.sort()

	print(p1)
	print(p2[len(p2)//2])
