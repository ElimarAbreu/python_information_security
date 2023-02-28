import hashlib

string=input('Digite o texto a ser gerado a hash: ')

dicionario={'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha256':hashlib.sha256, 'sha512':hashlib.sha512}
lista=list(dicionario.keys())

menu=int(input(''' #### MENU - ESCOLHA O TIPO de HASH ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
Digite o número do hash a ser gerado: '''))

try:
	menu-=1
	resultado=dicionario[lista[menu]](string.encode('utf-8'))
	print(f'A hash {lista[menu]} de "{string}" é: {resultado.hexdigest()}')
except:
	print('Opção inválida!')