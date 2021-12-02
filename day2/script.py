
with open('day2/in.txt') as f:
	lines = f.readlines()

	x = 0
	y = 0

	for line in lines:
		(dir, n) = line.rstrip().split(' ')
		if dir == "forward":
			x += int(n)
		elif dir == "down":
			y += int(n)
		elif dir == "up":
			y -= int(n)
	
	print("Part 1:", x * y)

	pos = 0
	depth = 0
	aim = 0

	for line in lines:
		(dir, n) = line.rstrip().split(' ')
		if dir == "forward":
			pos += int(n)
			depth += aim * int(n)
		elif dir == "down":
			aim += int(n)
		elif dir == "up":
			aim -= int(n)
	
	print("Part 2:", pos * depth)
