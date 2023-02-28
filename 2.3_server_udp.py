#Importa a biblioteca socket (realiza o relacionamento com a placa de rede do SO)
import socket

# Variável que cria/recebe um objeto de conexão (família de protocolo, tipo)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

host = 'localhost'
port = 5432

#Faz a ligação entre cliente e servidor, por meio do obejto de conexão (s), ao informar host e porta
s.bind((host,port))
mensagem='Servidor: Olá, cliente! Tudo bem?'

#Se a ligação for bem sucessida
while 1:
    #Variáveis que recebem uma resposta de 4096 Bytes
    dados,end=s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem...')
        #Envia mensagem
        s.sendto(dados+(mensagem.encode()),end)