#Importa o módulo/biblioteca os (integra os programas e recursos do S.O)
import os
#Importa o módulo/biblioteca time
import time

#Abre o arquivo:
with open('hosts.txt') as file:
    #Váriavel que lê e armazena o arquivo carregado
    dump=file.read()
    #Coloca o arquivo em linhas separadas
    dump=dump.splitlines()
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-'*60)
        # Chama o módulo system da biblioteca os - comando ping (-n é o número de pacotes).
        os.system('ping -n 2 {}'.format(ip))
        print('-'*60)
        time.sleep(5)
