import hashlib

file1='a.txt'
file2='b.txt'

hash1=hashlib.new('ripemd160')
hash1.update(open(file1,'rb').read())

hash2=hashlib.new('ripemd160')
hash2.update( open(file2,'rb').read())

if hash1.digest()!=hash2.digest():
    print(f'O arquivo {file1} é diferente do arquivo {file2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'Os arquivos {file1} e {file2} são iguais')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())