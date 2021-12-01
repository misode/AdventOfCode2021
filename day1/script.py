
with open('day1/in.txt') as f:
	nums = [int(l) for l in f.readlines()]

	increased = 0
	last = nums[0]
	for n in nums:
		if n > last:
			increased += 1
		last = n
	print('Part 1:', increased)

	increased = 0
	last = None
	for i in range(len(nums) - 2):
		sum = nums[i] + nums[i+1] + nums[i+2]
		if last is not None and sum > last:
			increased += 1
		last = sum
	print('Part 2:', increased)
