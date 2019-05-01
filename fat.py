def fat_iterativo(i):
	fat_vet = [None]*(i+1)
	fat_vet[0] = 1
	for n in range(1,i+1):
		fat_vet[n] = n * fat_vet[n-1]

	return fat_vet[i]

fat_4 = fat_iterativo(4)
print(fat_4)
