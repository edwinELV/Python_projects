#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pyautogui # Biblioteca que simula o mouse e o teclado
import time
import pyperclip

pyautogui.PAUSE = 1 # Precisa de dar uma pausa

# 1. Abrendo o navegador
pyautogui.press('winleft')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(25)
pyautogui.hotkey('winleft', 'up') # Maximizar janela
pyautogui.hotkey('ctrl', 't') # .hotkey -> Executa um atalho

# 2. Entrando a FAST
fast = 'https://fast.com'
pyperclip.copy(fast)
pyautogui.hotkey('ctrl', 'v') 
pyautogui.press('enter')
time.sleep(25)
pyautogui.click(x=1165, y=52)
time.sleep(5)
pyautogui.click(x=643, y=126)
time.sleep(5)
pyautogui.click(x=1040, y=601)
pyautogui.press('Esc')
pyautogui.hotkey('ctrl', 'w') 

# 3. Abrendo o zoom
pyautogui.press('winleft')
pyautogui.write('zoom')
pyautogui.press('enter')
time.sleep(160)
pyautogui.hotkey('winleft', 'up')  
time.sleep(5)
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)
pyautogui.write('Juan Carlos Tortoza') # Mudar sempre com um novo coordinador NO aceita carateres especias como til
time.sleep(2)
pyautogui.click(x=559, y=179)
time.sleep(5)
pyautogui.click(x=333, y=694)
pyautogui.hotkey('ctrl', 'v') 
pyautogui.press('enter')
time.sleep(2)
saludo = 'Buenos días, comenzando la jornada'
pyperclip.copy(saludo)
pyautogui.hotkey('ctrl', 'v') 
pyautogui.press('enter')

