import pyautogui as pt
import random
import secrets
import time
from datetime import datetime, timedelta
import numpy as np
import itertools 
from itertools import permutations  

#lista de possíveis tempos de pausa em segundos
random_pause = ['1', '1.3', '1.7', '2', '2.1', '2.4', '2.8', '3', '3.2', '3.5', '3.9', '4']

#----------------------------DEFININDO DURAÇÃO DE EXECUÇÃO---------------------------------#
start = datetime.now() #horário de início
time = input('quantas horas quer deixar o bot rodando?\n')\n #definir duração
end = (datetime.now() + timedelta(hours = time)).strftime('%H:%M:%S') #calcula quando parar o bot

time.sleep(secrets.choice(random_pause))

#----------------------------LOCALIZANDO BOTÕES E ATRIBUINDO VARIÁVEIS DE POSICIONAMENTO---------------------------------#
#atribui as posições dos botões
positions = []
for pos in pyautogui.locateAllOnScreen('someButton.png')
	positions = pos #[(1101, 252, 50, 50), (59, 481, 50, 50), (1395, 640, 50, 50)] #returns (left, top, width, height)

#----------------------------CONSTRUINDO MATRIZ DE RANDOMICIDADE---------------------------------#
#construir matriz randomica das 6 salas
x = []
y = []
for pos in positions: #criando range
	x = np.linspace(pos[0], pos[0]+pos[2]-1, pos[2])
	y = np.linspace(pos[1], pos[1]+pos[3]-1, pos[3])
	
	combinations = [] 
	permut = itertools.permutations(x, len(y)) 
	for comb in permut: 
	    zipped = zip(comb, y) 
	    combinations.append(list(zipped))	

#-------------------------------------LOOP DE REPETIÇÃO------------------------------------------#
#enquanto não alcançar o horário estimado, execute:
while datetime.now() < end:

	#clica em um botão aleatório
	mouse.click(secrets.choice(unique_combinations))
	
	#pausa aleatória
	time.sleep(secrets.choice(random_pause))

	se localizar combatente: 
		clica
	else: clica em sair
	
	#pausa aleatória
	time.sleep(secrets.choice(random_pause))

pyautogui.alert('Bot finalizado!')

