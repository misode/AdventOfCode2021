with open('day8/in.txt') as f:
	lines = [
		tuple(l.rstrip().split('|'))
		for l in f.readlines()]
	entries = [
		(i.strip().split(' '), o.strip().split(' '))
		for i, o in lines]

	p1 = 0
	p2 = 0
	for input, output in entries:
		lengths = [len(n) for n in output]
		p1 += lengths.count(2)
		p1 += lengths.count(3)
		p1 += lengths.count(4)
		p1 += lengths.count(7)

		one = next(n for n in input if len(n) == 2)
		four = next(n for n in input if len(n) == 4)
		seven = next(n for n in input if len(n) == 3)
		eight = next(n for n in input if len(n) == 7)

		A = next(iter(set(seven).difference(set(one))))

		counts = [0] * 7
		for i in input:
			for c in i:
				counts[ord(c) - ord('a')] += 1
		
		F = chr(counts.index(9) + ord('a'))
		candidates = [chr(i + ord('a')) for i, c in enumerate(counts) if c == 8]
		C = next(c for c in candidates if c != A)
		E = chr(counts.index(4) + ord('a'))

		two = next(n for n in input if F not in n)

		five = next(n for n in input if len(n) == 5 and C not in n)
		six = next(n for n in input if len(n) == 6 and C not in n)

		zero = next(n for n in input if len(n) == 6 and E in n and C in n)
		nine = next(n for n in input if len(n) == 6 and E not in n)

		three = next(n for n in input if len(n) == 5 and C in n and E not in n)

		digits = [set(d) for d in [zero, one, two, three, four, five, six, seven, eight, nine]]

		translated = ''.join([str(digits.index(set(n))) for n in output])
		p2 += int(translated)

	print(p1)
	print(p2)
