
def bingo(board, draws):
	for i in range(5):
		row = 0
		column = 0
		for j in range(5):
			if board[i][j] in draws:
				row += 1
			if board[j][i] in draws:
				column += 1
		if row == 5 or column == 5:
			return True

	return False
	

with open('day4/in.txt') as f:
	draws = [int(n) for n in f.readline().rstrip().split(',')]

	boards = []
	while f.readline():
		board = []
		for i in range(5):
			board.append([int(n) for n in f.readline().rstrip().split(' ') if n.isnumeric()])
		boards.append(board)

	last = len(boards)
	won = 0
	for i in range(len(draws)):
		drawn = set(draws[:i+1])
		for board in boards:
			if bingo(board, drawn):
				unmarked = [n for row in board for n in row if n not in drawn]
				won += 1
				if won == 1:
					print('Part 1:', sum(unmarked) * draws[i])
				if won == last:
					print('Part 2:', sum(unmarked) * draws[i])
				boards.remove(board)
		