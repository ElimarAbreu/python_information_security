#Importa a biblioteca socket (realiza o relacionamento com a placa de rede do SO)
import socket

#Variável que cria/recebe um objeto de conexão (familia de protocolo, tipo)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com sucesso.\n')

host='localhost'
port=5433
mensagem='Olá, servidor. Tudo certo?'

try:
	print('Cliente: '+mensagem)
	#Envia mensagem para o servidor.
        #enconde(): empacota a mensagem e a envia num pacote (udp) para o servidor.
	s.sendto(mensagem.encode(),(host,5432))

	#Variáveis que recebem do servidor uma resposta de 4096 Bytes
	dados,server=s.recvfrom(4096)
	#Variável que recebe os dados do servidor e desempacota
	dados=dados.decode()
	print('Cliente: '+dados)
finally:
	print('Cliente: Fechando a conexão')
	#Fecha a conexão.
	s.close()
