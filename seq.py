import pyautogui as pt
import random
import secrets
import time
from datetime import datetime, timedelta
import numpy as np
import itertools 
from itertools import permutations
from cv2 import imread

#lista de possíveis tempos de pausa em segundos
random_pause = np.arange(0.8, 4, 0.1))
pause = np.arange(0.5, 0.9, 0.1))

#----------------------------DEFININDO DURAÇÃO DE EXECUÇÃO---------------------------------#
start = datetime.now() #horário de início
time = input('quantas horas quer deixar o bot rodando?\n')\n #definir duração
end = (datetime.now() + timedelta(hours = time)).strftime('%H:%M:%S') #calcula quando parar o bot

time.sleep(secrets.choice(random_pause))
pt.moveTo(100, 100, 2, pt.easeOutQuad) 

#----------------------------LOCALIZANDO BOTÕES E ATRIBUINDO VARIÁVEIS DE POSICIONAMENTO---------------------------------#
#atribui as posições dos botões
positions = []
for pos in pt.locateAllOnScreen('someButton.png')
	positions = pos #[(1101, 252, 50, 50), (59, 481, 50, 50), (1395, 640, 50, 50)] #returns (left, top, width, height)

#----------------------------CONSTRUINDO MATRIZ DE RANDOMICIDADE---------------------------------#
x = []
y = []
#calcula range de coordenadas
for pos in positions: #criando range
	x = np.linspace(pos[0], pos[0]+pos[2]-1, pos[2])
	y = np.linspace(pos[1], pos[1]+pos[3]-1, pos[3])
	#faz a combinação entre cada coordenada x e y de cada botão para formar a matriz de possibilidades
	combinations = [] 
	permut = itertools.permutations(x, len(y)) 
	for comb in permut: 
	    zipped = zip(comb, y) 
	    combinations.append(list(zipped))	    
pt.moveTo(secrets.choice(unique_combinations), 2, pt.easeOutQuad)

#-------------------------------------LOOP DE REPETIÇÃO------------------------------------------#
#enquanto não alcançar o horário estimado, execute:
while datetime.now() < end:
	#movimento aleatório de mouse
	pt.moveTo(secrets.choice(unique_combinations))
	#pausa aleatória
	time.sleep(secrets.choice(random_pause))
		
	#escolhe uma das coordenadas da matriz de possibilidades e atribui efeito no mouse
	pt.moveTo(secrets.choice(unique_combinations), 2, pt.easeInElastic)
	pyautogui.click()
	time.sleep(secrets.choice(random_pause))

	if pt.locateOnScreen('C:/Program Files/Karim/Others/escolha1.png', region=(4,25,1360,1080), grayscale=True, confidence=0.5) != None:
		sc4 = pt.locateCenterOnScreen('escolha1.png', region=(4,25,1360,1080), confidence=0.9)
		pt.click(sc4)
		time.sleep(secrets.choice(pause))
		sc1 = pt.locateCenterOnScreen('porrada1.png', region=(4,25,1360,1080), confidence=0.7)
		pt.moveTo(sc1.x,sc1.y,0.11)
		pt.click(sc1)
		time.sleep(secrets.choice(pause))
		sc3 = pt.locateCenterOnScreen('atacar1.png', region=(4,25,1360,1080), confidence=0.9)
		pt.moveTo(sc3.x,sc3.y,0.15)
		pt.click(sc3)
		time.sleep(secrets.choice(pause))
		
		#movimento aleatório de mouse
		pt.moveTo(secrets.choice(unique_combinations))
		#pausa aleatória
		time.sleep(secrets.choice(random_pause))
	else: 
		sair = pt.locateCenterOnScreen('sair.png', region=(4,25,1360,1080), confidence=0.9)
		pt.moveTo(sair.x,sair.y,0.15)
		pt.click(sair)
		time.sleep(secrets.choice(pause))
	
	#movimento aleatório de mouse
	pt.moveTo(secrets.choice(unique_combinations))
	#pausa aleatória
	time.sleep(secrets.choice(random_pause))
pt.alert('Bot finalizado!')

