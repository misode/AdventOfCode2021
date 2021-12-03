
with open('day3/in.txt') as f:
	lines = [line.rstrip() for line in f.readlines()]

	bits = [0] * len(lines[0])

	for line in lines:
		for i, char in enumerate(line):
			if char == '1':
				bits[i] += 1

	gamma = ""
	epsilon = ""
	N = len(lines)/2
	for bit in bits:
		gamma += '1' if bit > N else '0'
		epsilon += '1' if bit < N else '0'
	
	print('Part 1:', int(gamma, 2) * int(epsilon, 2))

	possible = set(lines)
	i = 0
	while len(possible) > 1:
		bit = [line[i] for line in possible].count('1')
		allowed = '1' if bit >= len(possible)/2 else '0'
		possible = set(filter(lambda l: l[i] == allowed, possible))
		i += 1
	oxygen = int("".join(possible), 2)

	possible = set(lines)
	i = 0
	while len(possible) > 1:
		bit = [line[i] for line in possible].count('0')
		allowed = '0' if bit <= len(possible)/2 else '1'
		possible = set(filter(lambda l: l[i] == allowed, possible))
		i += 1
	carbon = int("".join(possible), 2)

	print('Part 2:', oxygen * carbon)

		