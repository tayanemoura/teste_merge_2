def fat(i):
	if i< 1:
		return 1
	else:
		fat_i =  i * fat(i-1)
		return fat_i

fat(4)
