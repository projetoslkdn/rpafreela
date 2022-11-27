#código em desenvolvimento

import pyautogui as pt
import random
import secrets
import time
from datetime import datetime, timedelta

#lista de pausa
random_pause = ['1', '2', '3', '4', '5']

#localiza horário inicial
start = datetime.now()

#definir duração
time = input('quantas horas quer deixar o bot rodando?\n') \n

#define quando parar o bot
end = (datetime.now() + timedelta(hours = time)).strftime('%H:%M:%S')

#pausa aleatória
time.sleep(secrets.choice(random_pause))

#enquanto não alcançar o horário estimado, execute:
while datetime.now() < end:

	#atribui as posições dos botões
	positions = []
	for pos in pyautogui.locateAllOnScreen('someButton.png')
		positions = pos
	list(pyautogui.locateAllOnScreen('someButton.png'))
	[(1101, 252, 50, 50), (59, 481, 50, 50), (1395, 640, 50, 50), (1838, 676, 50, 50)] #returns (left, top, width, height) - numeros de exemplo

	#escolhe aleatóriamente um dos botôes e clica fazendo firula
	mouse.click(secrets.choice(positions))
	
	#pausa aleatória
	time.sleep(secrets.choice(random_pause))

	se localizar combatente: 
		clica
	else: clica em sair

	time.sleep(secrets.choice(random_pause))

3mensagem de alerta ao alcançar o horário pre-determinado
pyautogui.alert('Bot finalizado!')




