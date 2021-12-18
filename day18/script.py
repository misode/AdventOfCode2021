import json
import math
from itertools import product
from copy import deepcopy

def add(a, b):
	return reduce([a, b])

def iter(sf, path=[]):
	if isinstance(sf, int):
		yield (sf, path)
	else:
		yield from iter(sf[0], [*path, 0])
		yield from iter(sf[1], [*path, 1])

def put(sf, path, value):
	if len(path) == 1:
		sf[path[0]] = value
	else:
		put(sf[path[0]], path[1:], value)

def reduce(sf):
	while True:
		reducing = False
		S = list(iter(sf))
		for i, (v, p) in enumerate(S):
			if len(p) > 4:
				(v2, _) = S[i+1]
				if i > 0:
					(lv, lp) = S[i-1]
					put(sf, lp, lv + v)
				if i < len(S)-2:
					(rv, rp) = S[i+2]
					put(sf, rp, rv + v2)
				put(sf, p[:-1], 0)
				reducing = True
				break
		if not reducing:
			for v, p in S:
				if v >= 10:
					put(sf, p, [math.floor(v / 2), math.ceil(v / 2)])
					reducing = True
					break
		if not reducing:
			return sf

def mag(sf):
	if isinstance(sf, int):
		return sf
	return 3 * mag(sf[0]) + 2 * mag(sf[1])

lines = open('day18/in.txt').readlines()
SF = [json.loads(line) for line in lines]

summed = 0
for sf in SF:
	summed = add(summed, deepcopy(sf))
print(mag(summed))

maximum = 0
for i, j in product(SF, SF):
	reduced = add(deepcopy(i), deepcopy(j))
	maximum = max(maximum, mag(reduced))
print(maximum)
