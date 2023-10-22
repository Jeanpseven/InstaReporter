import time
from webbot import *
import pyautogui

import argparse
import sys

# Para analisar os argumentos
def obterOpcoes(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="Este bot ajuda os usuários a denunciar em massa contas com iscas de clique ou conteúdo objetável no Instagram.")
    parser.add_argument("-u", "--usuario", type=str, default="", help="Nome de usuário para denunciar.")
    parser.add_argument("-f", "--arquivo", type=str, default="contas.txt", help="Lista de contas (Padrão é contas.txt no diretório do programa).")

    opcoes = parser.parse_args(args)

    return opcoes

# Verifica se a opção de ajuda foi fornecida
if "-h" in sys.argv or "--help" in sys.argv:
    print("Este script ajuda a denunciar em massa contas com iscas de clique ou conteúdo objetável no Instagram.")
    print("Opções disponíveis:")
    print("-u, --usuario: Nome de usuário para denunciar (obrigatório).")
    print("-f, --arquivo: Nome do arquivo de contas (padrão é 'contas.txt' no diretório do programa).")
    sys.exit(0)

args = obterOpcoes()

usuario = args.usuario
arquivo_contas = args.arquivo

if usuario == "":
    usuario = input("Nome de usuário: ")

print("Certifique-se de que o arquivo contas.txt contenha credenciais de conta no seguinte formato:")
print("nome_de_usuário:senha")

a = open(arquivo_contas, "r").readlines()
linhas = [s.rstrip() for s in a]
linhas.reverse()

usuarios = []
senhas = []
for linha in linhas:
    partes = linha.split(":")
    nome_usuario = partes[0]
    senha = partes[1]
    usuarios.append(nome_usuario)
    senhas.append(senha)

while True:  # Loop infinito para denunciar em loop
    for indice in range(len(linhas) + 1):
        web = Browser()
        web.go_to("https://www.instagram.com/accounts/login/")

        web.type(usuarios[indice], into='Número de telefone, nome de usuário ou email')
        time.sleep(0.5)
        web.press(web.Key.TAB)
        time.sleep(0.5)
        web.type(senhas[indice], into='Senha')
        web.press(web.Key.ENTER)

        time.sleep(2.0)

        web.go_to("https://www.instagram.com/%s/" % usuario)

        time.sleep(1.5)

        web.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')

        time.sleep(0.5)

        web.click(text='Denunciar Usuário')

        time.sleep(1.5)

        web.click(xpath="/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]")

        time.sleep(0.5)

        web.click(text='Fechar')

        time.sleep(0.5)

        web.click(xpath='/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')

        time.sleep(0.5)

        web.click(xpath='/html/body/div[1]/section/main/div/header/section/div[1]/div/button')

        time.sleep(0.5)

        web.click(text='Sair')

        time.sleep(0.5)

        pyautogui.keyDown('ctrl')
        time.sleep(0.25)
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('w')
