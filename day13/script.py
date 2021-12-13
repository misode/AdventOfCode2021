with open('day13/in.txt') as f:
	G = set()
	F = []
	for line in f.readlines():
		if line[0].isdigit():
			G.add(tuple([int(p) for p in line.rstrip().split(',')]))
		elif line.startswith("fold"):
			F.append((line[11], int(line.rstrip()[13:])))

	for i, (d, f) in enumerate(F):
		H = set()
		for (x, y) in G:
			if d == 'x' and x > f:
				H.add((f-(x-f), y))
			elif d == 'y' and y > f:
				H.add((x, f-(y-f)))
			else:
				H.add((x, y))
		G = H
		if i == 0:		
			print(len(G))

	for y in range(6):
		print(''.join(['#' if (x, y) in H else ' ' for x in range(39)]))
