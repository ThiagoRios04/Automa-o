# Passo 1- Entrar no sistema da empresa
# link:https://dlp.hashtagtreinamentos.com/python/intensivao/login
#passo 2-Fazer login
#passo 3- Pegar/Importar a base de dados
#passo 4- Cadastrar um produto
#Passo 5- Repetiro passo 4 até cadastrar todos os produtos
# pip install pyautogui


import pyautogui
import time

#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey
#pyautogui.scroll

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=970, y=472)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('testeaula@gmail.com')
pyautogui.press('tab')

pyautogui.write('test')
pyautogui.click(x=968, y=659)
time.sleep(2)

import pandas
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=682, y=320)
    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if obs != 'nan':
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
    










    



















