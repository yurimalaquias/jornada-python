# RPA - Automacao de processos

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 1
time.sleep(0.2)

# abre o spotilight macos
pyautogui.hotkey("command", "space", interval=0.1)

# digita o nome do software e abre
pyautogui.write("safari")
pyautogui.press("enter")

# abre a barra de endereco macos
pyautogui.hotkey("command", "l", interval=0.1)

# digita o link e acessa
pyautogui.write(link)
pyautogui.press("enter")

#aguarda 5 segundos
time.sleep(5)

# clica no campo de email
pyautogui.click(x=650, y=361)

# digita o email
pyautogui.write("pythonteste@gmail.com")
pyautogui.press("tab")

# digita a senha
pyautogui.write("123qwe")

# click no botao enviar
pyautogui.click(x=726, y=535)

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:
    # clica no primeiro input do formulario
    pyautogui.click(x=632, y=258)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # isna = verifica se é NaN
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    # envia o formulario
    pyautogui.press("enter")

    pyautogui.scroll(5000)