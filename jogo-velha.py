import time
import random
import os

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    limparTela()
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
    print("-------------")
    print("| 4 | 5 | 6 |")
    print("-------------")
    print("| 7 | 8 | 9 |")
    print("-------------")
    print("A cada rodada, você poderá inserir a sua opção apenas nos espaços vazios.")
    print("Pressione <ENTER> para continuar.")
    input()

def escolhaJogador():
#    limparTela()
    while True:
        print("VAMOS JOGAR!")
        escolha = input("Você quer jogar com (X) ou com (O)? ").capitalize()
        if escolha in ["X", "O"]:
            if escolha == "X":
                return escolha, "O"
            else:  # Se a escolha for "O"
                return escolha, "X"
        print("Opção inválida. Insira apenas \"X\" ou \"O\". Tente novamente.")
        time.sleep(3)
        limparTela()

def indiceTabuleiro():
    while True:
        try:
            indice = int(input("Indique a posição em que você quer fazer a sua jogada: "))
            if 1 <= indice <= 9:
                return indice - 1
            else:
                print("Insira apenas números de 1 a 9. Tente novamente.")
                time.sleep(3)
                limparTela()
                break
        except ValueError:
            print("Insira apenas números de 1 a 9. Tente novamente.")
            time.sleep(3)
            limparTela()
    return indice - 1

def imprimirTabuleiro(tabuleiro):
    print("-------------")
    for i in range(0, 9, 3):  # Percorre o tabuleiro em passos de 3
        linha = "| "
        for j in range(3):  # Percorre cada segmento de 3 índices para formar uma linha
            if tabuleiro[i + j] is None:
                linha += "  | "  # Espaço em branco para None
            else:
                linha += str(tabuleiro[i + j]) + " | "  # Valor do tabuleiro
        print(linha)
        print("-------------")

def verificarVencedor(tabuleiro, jogador):
    vitorias = [
        (0, 1, 2),  # Linha superior
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # Coluna da esquerda
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # Diagonal esquerda para baixo
        (2, 4, 6)
    ]
    
    for vitoria in vitorias:
        venceu = True
        for i in vitoria:
            if tabuleiro[i] != jogador:
                venceu = False
                break
        if venceu:
            return True
    return False

# os.system("cls" if os.name == "nt" else "clear")

cabecalho()

instrucoes()

tabuleiro = [None] * 9

opcaoJogador, opcaoComp = escolhaJogador()

while any(item is None for item in tabuleiro):

    print("Tabuleiro atual:")
    imprimirTabuleiro(tabuleiro)

    if verificarVencedor(tabuleiro, opcaoJogador):
        print("Parabéns! Você venceu!")
        time.sleep(3)
        limparTela()
        break
    elif verificarVencedor(tabuleiro, opcaoComp):
        print("O computador venceu. Tente novamente!")
        time.sleep(3)
        limparTela()
        break
    else:
        indiceJogador = indiceTabuleiro()

        indiceDiferente = True

        if tabuleiro[indiceJogador] == None:
            tabuleiro[indiceJogador] = opcaoJogador
        else:
            print("\nATENÇÃO! Esta posição do tabuleiro já está ocupada. Escolha outra posição no tabuleiro.")
            time.sleep(3)
            limparTela()
            continue

        while True:
            if all(item is not None for item in tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                time.sleep(3)
                limparTela()
                break
            indiceComp = random.randint(0, 8)
            if tabuleiro[indiceComp] == None:
                tabuleiro[indiceComp] = opcaoComp
                break
            else:
                continue


