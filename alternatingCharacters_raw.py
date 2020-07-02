
s = 'AAABBB'

s = [i for i in s]

contador = 0

quien_compara = s[0]

for i in s[1:]:

	if quien_compara == i:

		contador +=1

	else:

		quien_compara = i


print(contador)

	