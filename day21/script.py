import itertools
import functools

# INPUT = (4, 8)
INPUT = (10, 2)

last = 0
rolls = 0
def roll():
	global last
	global rolls
	last = (last % 100) + 1
	rolls += 1
	return last

def play1(state):
	while True:
		for i, (pos, score) in enumerate(state):
			move = roll() + roll() + roll()
			newPos = (pos + move) % 10
			newScore = score + newPos + 1
			state[i] = (newPos, newScore)
			if newScore >= 1000:
				return rolls * state[1 - i][1]

MOVES = [sum(rolls) for rolls in itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3])]

@functools.cache
def play2(ownPos, ownScore, otherPos, otherScore):
		wins = (0, 0)
		for move in MOVES:
				newPos = (ownPos + move) % 10
				newScore = ownScore + newPos + 1
				if newScore >= 21:
					wins = (wins[0] + 1, wins[1])
				else:
					otherWins, ownWins = play2(otherPos, otherScore, newPos, newScore)
					wins = (wins[0] + ownWins, wins[1] + otherWins)
		return wins

print(play1([(INPUT[0] - 1, 0), (INPUT[1] - 1, 0)]))
print(max(play2(INPUT[0] - 1, 0, INPUT[1] - 1, 0)))
