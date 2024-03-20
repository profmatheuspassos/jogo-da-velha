import time
import random
import os

def cabecalho():
    os.system("cls" if os.name == "nt" else "clear")
    print("=============================")
    print("Bem-vindo(a) ao Jogo da Velha")
    print("=============================")
    print("\n")

def instrucoes():
    print("INSTRUÇÕES")
    print("A cada jogada, iremos pedir que você indique um número entre 1 e 9.")
    print("Os números correspondem à posição em que você quer que a jogada seja feita.")
    print("Veja abaixo a posição dos números no tabuleiro:")
    print("-------------")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print("-------------")
    print("A cada rodada, você poderá inserir a sua opção apenas nos espaços vazios.")
    print("Pressione <ENTER> para continuar.")

def escolhaJogador():
    os.system("cls" if os.name == "nt" else "clear")
    print("VAMOS JOGAR!")
    print("Você quer jogar com (X) ou com (O)?")
    escolha = input("Indique sua opção: ").capitalize()
    return escolha

def indiceTabuleiro():
    while True:
        try:
            indice = int(input("Indique a posição em que você quer fazer a sua jogada: "))
            if indice not in range(1, 10):
                print("Insira apenas números de 1 a 9. Tente novamente.")
                time.sleep(3)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                break
        except ValueError:
            print("Insira apenas números de 1 a 9. Tente novamente.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
    return indice - 1

os.system("cls" if os.name == "nt" else "clear")

# cabecalho()

# instrucoes()

tabuleiro = [None] * 9

while True:
    opcaoJogador = escolhaJogador()
    if opcaoJogador == "X":
        opcaoComp = "O"
    elif opcaoJogador == "O":
        opcaoComp = "X"
    else:
        print("Opção inválida. Insira apenas \"X\" ou \"O\". Tente novamente.")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        continue
    break

indiceJogador = indiceTabuleiro()
indiceComp = random.randint(0, 8)

print(f"Opção jogador: {opcaoJogador}")
print(f"Opção compputador: {opcaoComp}")
print(f"Posição escolhida jogador: {indiceJogador}")
print(f"Posição escolhida computador: {indiceComp}")