#Importa o módulo/biblioteca os (integra os programas e recursos do S.O)
import os

#Váriável que recebe o endereço IP
ip_ou_host=input('Digite o IP ou host a ser verificado: ')

print('#'*60)
#Chama o módulo system da biblioteca os - comando ping (-n é o número de pacotes).
os.system('ping -n 6 {}'.format(ip_ou_host))
print('#'*60)
