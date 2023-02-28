from threading import Thread
import time

def carro(v,p):
	x=0
	while x<=100:
		x+=v
		time.sleep(0.5)
		print('Piloto: {} Km: {} \n'.format(p,x))

t_carro1 = Thread(target=carro, args=[1,'PilotoA'])
t_carro2 = Thread(target=carro, args=[2.5,'PilotoB'])

t_carro1.start()
t_carro2.start()