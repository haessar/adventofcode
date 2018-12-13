# 1.1
def iter_freq():
	with open('1.txt') as f:
		while True:
			try:
				yield int(f.readline())
			except ValueError:
				break

print sum(iter_freq())


# 1.2
def iter_cumsum(gen, init=0):
    cumsum = init
    for freq in gen:
        cumsum += freq
        yield cumsum

def first_duplicate_freq():
	counter = set()
	idx = 1
	init = 0
	while True:	
		for f in iter_cumsum(iter_freq(), init):
			counter.add( f )
			if len(counter) < idx:
				return f
			idx += 1
		init = f

print first_duplicate_freq()
