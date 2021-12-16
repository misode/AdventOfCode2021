import math

with open('day16/in.txt') as f:
	msg = f.readline().rstrip()
	bits = bin(int('F' + msg, 16))[6:]

	def read():
		global i
		global p1
		version = int(bits[i:i+3], 2)
		p1 += version
		i += 3
		type = int(bits[i:i+3], 2)
		i += 3
		if type == 4:
			groups = ''
			ends = 1
			while ends:
				ends = int(bits[i])
				groups += bits[i+1:i+5]
				i += 5
			value = int(groups, 2)
			return value
		else:
			length_id = int(bits[i])
			n = 15 if length_id == 0 else 11
			i += 1
			length = int(bits[i:i+n], 2)
			i += n
			values = []
			if length_id == 0:
				start = i
				while i-start < length:
					values.append(read())
			else:
				assert length_id == 1
				for _ in range(length):
					values.append(read())
			if type == 0:
				return sum(values)
			elif type == 1:
				return math.prod(values)
			elif type == 2:
				return min(values)
			elif type == 3:
				return max(values)
			elif type == 5:
				return int(values[0] > values[1])
			elif type == 6:
				return int(values[0] < values[1])
			elif type == 7:
				return int(values[0] == values[1])

	i = 0
	p1 = 0
	p2 = read()

	print(p1)
	print(p2)
