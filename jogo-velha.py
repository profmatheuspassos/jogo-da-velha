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
    print("Pressione <ENTER> para continuar.")
        

os.system("cls" if os.name == "nt" else "clear")

jogadas = ["X", "O"]
linha1 = [None, None, None]
linha2 = [None, None, None]
linha3 = [None, None, None]
# for _ in range(3):
    # linha1.append(random.choice(jogadas))
    # linha2.append(random.choice(jogadas))
    # linha3.append(random.choice(jogadas))
# print(linha1)
# print(linha2)
# print(linha3)

while True:
    print("Você quer jogar com (X) ou com (O)?")
    escolha = input("Indique sua opção: ").capitalize()
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
                print(linha1)
                print(linha2)
                print(linha3)
                break
        except:
            print("Insira apenas números de 1 a 9. Voltando ao menu principal...")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            continue