import heapq as q

with open('day15/in.txt') as f:
	grid = [[int(c) for c in l.rstrip()] for l in f.readlines()]

	def solve(T):
		N = len(grid)
		D = [[None] * T*N for _ in range(T*N)]
		Q = []
		q.heappush(Q, (0, 0, 0))
		D[0][0] = 0

		while Q:
			n, x, y = q.heappop(Q)
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				xx, yy = x+dx, y+dy
				if 0<=xx<T*N and 0<=yy<T*N and D[yy][xx] is None:
					g = grid[yy % N][xx % N]
					g += xx // N + yy // N - 1
					g = (g % 9) + 1
					q.heappush(Q, (n+g, xx, yy))
					D[yy][xx] = n+g

		return D[T*N-1][T*N-1]

	print(solve(1))
	print(solve(5))
