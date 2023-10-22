from requests import Session
from random import choice
from os import path
from multiprocessing import Process
from colorama import Fore, Back, Style

# Funções adicionadas
def VerificarIPPublico():
    try:
        with Session() as ses:
            res = ses.get("https://api.ipify.org/?format.json")
            if res.status_code == 200:
                return res.json()["ip"]
            return None
    except:
        return None

def ProxyFuncionando(proxy):
    try:
        with Session() as ses:
            ses.proxies.update(proxy)
            res = ses.get("https://api.ipify.org/?format.json")
            if res.status_code == 200:
                if res.json()["ip"] != VerificarIPPublico() and VerificarIPPublico() is not None:
                    return True
            return False
    except:
        return False

# Funções de impressão
def ImprimirSucesso(mensagem, nome_usuario, *argv):
    print("[ OK ] ", end="")
    print("[", end="")
    print(nome_usuario, end="")
    print("] ", end="")
    print(mensagem, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def ImprimirOpcoes():
    print("""    
    +----------------------------+--------+
    |        Motivo              | Número |
    +----------------------------+--------+
    | Spam                       |      1 |
    | Não se machucar            |      2 |
    | Drogas                     |      3 |
    | Nudez                      |      4 |
    | Gravidade                  |      5 |
    | Discurso de ódio           |      6 |
    | Assédio e Bullying         |      7 |
    | Imitação de identidade     |      8 |
    | Criança menor de idade     |     11 |
    +----------------------------+--------+
    """)

def ObterEntrada(mensagem, *argv):
    print("[ ? ] ", end="")
    print(mensagem, end=" ")
    for arg in argv:
        print(arg, end=" ")
    return input()

def ImprimirErroFatal(mensagem, *argv):
    print("[ X ] ", end="")
    print(mensagem, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def ImprimirErro(mensagem, nome_usuario, *argv):
    print("[ X ] ", end="")
    print("[", end="")
    print(nome_usuario, end="")
    print("] ", end="")
    print(mensagem, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def ImprimirStatus(mensagem, *argv):
    print("[ * ] ", end="")
    print(mensagem, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

# Restante do código principal
def dividir_em_blocos(lst, n):
    """Gera blocos de tamanho n a partir da lista lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def processo_ataque_perfil(nome_usuario, lista_proxies):
    if len(lista_proxies) == 0:
        for _ in range(10):
            report_profile_attack(nome_usuario, None)
        return

    for proxy in lista_proxies:
        report_profile_attack(nome_usuario, proxy)

def processo_ataque_video(url_video, lista_proxies):
    if len(lista_proxies) == 0:
        for _ in range(10):
            report_video_attack(url_video, None)
        return

    for proxy in lista_proxies:
        report_video_attack(url_video, proxy)

def ataque_video(proxies):
    url_video = ObterEntrada("Digite o link do vídeo que deseja denunciar:")
    print(Style.RESET_ALL)
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=processo_ataque_video, args=(url_video, [],))
            p.start()
            print_status(str(k + 1) + ". Processo Iniciado!")
            if k == 5:
                print()
        return

    blocos = list(dividir_em_blocos(proxies, 10))

    print("")
    print_status("Iniciando ataque de denúncia de vídeo!\n")

    i = 1
    for lista_proxies in blocos:
        p = Process(target=processo_ataque_video, args=(url_video, lista_proxies,))
        p.start()
        print_status(str(i) + ". Processo Iniciado!")
        if k == 5:
            print()
        i = i + 1

def ataque_perfil(proxies):
    nome_usuario = ObterEntrada("Digite o nome de usuário que deseja denunciar:")
    print(Style.RESET_ALL)
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=processo_ataque_perfil, args=(nome_usuario, [],))
            p.start()
            print_status(str(k + 1) + ". Processo Iniciado!")
        return

    blocos = list(dividir_em_blocos(proxies, 10))

    print("")
    print_status("Iniciando ataque de denúncia de perfil!\n")

    i = 1
    for lista_proxies in blocos:
        p = Process(target=processo_ataque_perfil, args=(nome_usuario, lista_proxies,))
        p.start()
        print_status(str(i) + ". Processo Iniciado!")
        if k == 5:
            print()
        i = i + 1

def main():
    print_success("Módulos carregados!\n")

    ret = ObterEntrada("Deseja usar proxies? [S/N]")

    proxies = []

    if ret == "S" or ret == "s":
        ret = ObterEntrada("Deseja coletar proxies da internet? [S/N]")

        if ret == "S" or ret == "s":
            print_status("Coletando proxies da internet. Isso pode levar um tempo.\n")
            proxies = find_proxies()
        elif ret == "N" or ret == "n":
            print_status("Por favor, coloque um máximo de 50 proxies em um arquivo!")
            caminho_arquivo = ObterEntrada("Digite o caminho do seu arquivo de proxies:")
            proxies = parse_proxy_file(caminho_arquivo)
        else:
            print_error("Resposta não compreendida. Saindo!")
            exit()

        print_success(str(len(proxies)) + " proxies encontrados!\n")
    elif ret == "N" or ret == "n":
        pass
    else:
        print_error("Resposta não compreendida. Saindo!")
        exit()

    print("")
    print_status("1 - Denunciar perfil.")
    print_status("2 - Denunciar um vídeo.")
    escolha_denuncia = ObterEntrada("Escolha o método de denúncia")
    print("")

    if not escolha_denuncia.isdigit():
        print_error("Resposta não compreendida.")
        exit(0)

    escolha_denuncia = int(escolha_denuncia)

    if escolha_denuncia > 2 or escolha_denuncia == 0:
        print_error("Resposta não compreendida.")
        exit(0)

    if escolha_denuncia == 1:
        ataque_perfil(proxies)
    elif escolha_denuncia == 2:
        ataque_video(proxies)

if __name__ == "__main__":
    print_success("Modo de Imagem!")
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] Encerrando o programa!")
        print(Style.RESET_ALL)
        _exit(0)
