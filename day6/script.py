def simulate(state, days):
	for _ in range(days):
		n = state[0]

		state[0] = state[1]
		state[1] = state[2]
		state[2] = state[3]
		state[3] = state[4]
		state[4] = state[5]
		state[5] = state[6]
		state[6] = state[7]
		state[7] = state[8]

		state[8] = n
		state[6] += n

	return sum(state)

with open('day6/in.txt') as f:
	fish = [int(e) for e in f.readline().rstrip().split(',')]

	state = [fish.count(i) for i in range(9)]

	print('Part 1:', simulate(state.copy(), 80))
	print('Part 2:', simulate(state.copy(), 256))
