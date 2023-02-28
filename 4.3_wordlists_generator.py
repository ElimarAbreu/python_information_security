import itertools

string=input('String a ser permutada: ')
len_resultado=len(string)
resultado = itertools.permutations(string,len_resultado)

for i in resultado:
	print(''.join(i))