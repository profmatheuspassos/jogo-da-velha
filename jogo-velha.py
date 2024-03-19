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
    print("Você quer jogar com (X) ou com (O)?")
    escolha = input("Indique sua opção: ").capitalize()
    return escolha

os.system("cls" if os.name == "nt" else "clear")

jogadas = ["X", "O"]
linha1 = [None, None, None]
linha2 = [None, None, None]
linha3 = [None, None, None]

escolha = escolhaJogador()

while True:
    if escolha not in ["X", "O"]:
        print("Insira apenas X ou O. Voltando ao menu principal...")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        continue
    else:
        print(f"Você escolheu a opção {escolha}.")
        print("Vamos começar! Mas antes, leia com atenção as instruções abaixo.\n")
        instrucoes()
        input()
        try:
            posicao = int(input("Indique em qual posição você quer fazer a sua jogada: "))
        except:
            print("Insira apenas números de 1 a 9. Voltando ao menu principal...")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            continue
        if posicao not in range(1, 10):
            print("Insira apenas números de 1 a 9. Voltando ao menu principal...")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            continue
        else:
            linha = (posicao - 1) // 3
            indice = (posicao - 1) % 3
            if linha == 0:
                linha1[indice] = escolha
            elif linha == 1:
                linha2[indice] = escolha
            elif linha == 2:
                linha3[indice] = escolha
            while True:
                posicaoComp = random.choice(range(1, 10))
                escolhaComp = random.choice(["X", "O"])
                if posicaoComp == posicao:
                    continue
                else:
                    linhaComp = (posicaoComp - 1) // 3
                    indiceComp = (posicaoComp - 1) % 3
                    if linhaComp == 0:
                        if None in linha1:
                            if linha1[indiceComp] == None:
                                linha1[indiceComp] = escolhaComp
                            else:
                                continue
                        else:
                            pass
                    elif linhaComp == 1:
                        if None in linha2:
                            if linha2[indiceComp] == None:
                                linha2[indiceComp] = escolhaComp
                            else:
                                continue
                        else:
                            pass
                    elif linhaComp == 2:
                        if None in linha3:
                            if linha3[indiceComp] == None:
                                linha3[indiceComp] = escolhaComp
                            else:
                                continue
                        else:
                            pass
                print(linha1)
                print(linha2)
                print(linha3)
                break
            break
    