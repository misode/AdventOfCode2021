with open('day17/in.txt') as f:
	# (tx0, tx1, ty0, ty1) = (20, 30, -10, -5)
	(tx0, tx1, ty0, ty1) = (277, 318, -92, -53)

	p1 = 0
	p2 = 0

	for vx0 in range(1, 400):
		for vy0 in range(-200, 100):
			x, y = 0, 0
			vx, vy = vx0, vy0
			top = y

			for i in range(1000):
				x += vx
				y += vy
				vx -= 1 if vx > 0 else 0
				vy -= 1
				top = max(top, y)

				if x > tx1 or y < ty0:
					break
				if x >= tx0 and y <= ty1:
					p2 += 1
					if top > p1:
						p1 = max(p1, top)
					break

	print(p1)
	print(p2)
