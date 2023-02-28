#Importa a biblioteca socket (realiza o relacionamento com a placa de rede do SO)
import socket
#Importa a biblioteca sys (fornece acesso a variáveis/funcões com relação com o intepretador python)
import sys

def main():
	try:
        #Variável que recebe um objeto de conexão (familia de protocolo, tipo, protocolo)
	    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	except socket.error as e:
		print('Conexão falhou!')
		print('Erro: {}'.format(e))
        #Sai da aplicação
		sys.exit()
	print('Socket criado com sucesso')

	host_alvo=input('Digite o host ou IP a ser conectado: ')
	port_alvo=input('Digite a porta a ser conectada: ')

	try:
        #Objeto que realiza a conexão, por meio do ip e porta informados
		s.connect((host_alvo,int(port_alvo)))
		print('Client TCP conectado com sucesso no host '+host_alvo+' e na porta '+port_alvo)
        #Desliga a conexão, após 2s.
		s.shutdown(2)
	except socket.error as e:
		print('Não foi possível conectar no host: '+host_alvo+' - Porta: '+port_alvo)
		print('Erro: {}'.format(e))
		sys.exit()

if __name__ == '__main__':
	main()