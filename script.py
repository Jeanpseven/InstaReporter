import time
from webbot import Browser
import pyautogui
import argparse
import sys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

# Função para verificar se uma conta existe
def verificar_conta_existe(conta):
    url = f"https://www.instagram.com/{conta}/"
    response = requests.get(url)
    return response.status_code == 200

def configurar():
    navegador = input("Digite o navegador a ser utilizado (chrome ou firefox): ").strip().lower()
    if navegador == "chrome":
        driver_path = ChromeDriverManager().install()
    elif navegador == "firefox":
        driver_path = GeckoDriverManager().install()
    else:
        print("Navegador não suportado. Use 'chrome' ou 'firefox'.")
        sys.exit(1)

    web = Browser(webdriver=navegador, driverpath=driver_path)
    return web

# Função para denunciar contas
def denunciar_contas(web, denunciantes, contas):
    for denunciante in denunciantes:
        web.go_to("https://www.instagram.com/accounts/login/")
        web.type(denunciante["usuario"], into="Número de telefone, nome de usuário ou email")
        web.press(web.Key.TAB)
        time.sleep(1)
        senha = denunciante["senha"]
        web.type(senha, into="Senha")
        web.press(web.Key.ENTER)
        time.sleep(3)

        for conta in contas:
            # Função para denunciar uma conta
            def denunciar_conta(conta):
                if verificar_conta_existe(conta):
                    web.go_to(f"https://www.instagram.com/{conta}/")
                    time.sleep(2)
                    web.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')
                    time.sleep(2)
                    web.click(text="Denunciar Usuário")
                    time.sleep(2)
                    web.click(xpath="/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]")
                    time.sleep(2)
                    web.click(text="Fechar")
                    time.sleep(2)
                else:
                    print(f"A conta {conta} não existe. Ignorando a denúncia.")

            denunciar_conta(conta)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Este bot ajuda os usuários a denunciar em massa contas com iscas de clique ou conteúdo objetável no Instagram.")
    parser.add_argument("-f", "--arquivo", type=str, default="contas.txt", help="Lista de contas (Padrão é 'contas.txt' no diretório do programa).")

    opcoes = parser.parse_args()
    arquivo_contas = opcoes.arquivo

    denunciantes = []
    quantidade_denunciantes = int(input("Quantidade de perfis denunciantes (padrão é 1): ") or 1)
    for i in range(quantidade_denunciantes):
        usuario = input(f"Nome de usuário do perfil denunciante {i + 1}: ").strip()
        senha = input(f"Senha do perfil denunciante {i + 1}: ").strip()
        denunciantes.append({"usuario": usuario, "senha": senha})

    web = configurar()
    contas = []

    quantidade_contas = int(input("Quantidade de contas a denunciar (padrão é 1): ") or 1)
    for i in range(quantidade_contas):
        nome_usuario = input(f"Nome de usuário da conta {i + 1}: ").strip()
        contas.append(nome_usuario)

    # Execute a função de denunciar contas
    denunciar_contas(web, denunciantes, contas)
