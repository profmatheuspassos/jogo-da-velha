import time
import random
import os

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [None] * 9
        self.jogador_atual = None
        self.oponente = None

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def cabecalho(self):
        self.limpar_tela()
        print("=============================")
        print("Bem-vindo(a) ao Jogo da Velha")
        print("=============================")
        print("\n")

    def instrucoes(self):
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

    def escolha_jogador(self):
        while True:
            print("VAMOS JOGAR!")
            escolha = input("Você quer jogar com (X) ou com (O)? ").capitalize()
            if escolha in ["X", "O"]:
                self.jogador_atual = escolha
                self.oponente = "O" if escolha == "X" else "X"
                return
            print("Opção inválida. Insira apenas \"X\" ou \"O\". Tente novamente.")
            time.sleep(3)
            self.limpar_tela()

    def indice_tabuleiro(self):
        while True:
            try:
                indice = int(input("Indique a posição em que você quer fazer a sua jogada: "))
                if 1 <= indice <= 9:
                    return indice - 1
            except ValueError:
                pass
            print("Insira apenas números de 1 a 9. Tente novamente.")
            time.sleep(3)
            self.limpar_tela()

    def imprimir_tabuleiro(self):
        print("-------------")
        for i in range(0, 9, 3):
            linha = "| "
            for j in range(3):
                valor = self.tabuleiro[i + j]
                linha += f"{valor if valor else ' '} | "
            print(linha)
            print("-------------")

    def verificar_vencedor(self, jogador):
        vitorias = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for vitoria in vitorias:
            if all(self.tabuleiro[i] == jogador for i in vitoria):
                return True
        return False

    def jogar(self):
        self.cabecalho()
        self.instrucoes()
        self.escolha_jogador()

        while any(item is None for item in self.tabuleiro):
            self.imprimir_tabuleiro()
            if self.verificar_vencedor(self.jogador_atual):
                print("Parabéns! Você venceu!")
                break
            elif self.verificar_vencedor(self.oponente):
                print("O computador venceu. Tente novamente!")
                break

            indice = self.indice_tabuleiro()
            if self.tabuleiro[indice] is None:
                self.tabuleiro[indice] = self.jogador_atual
            else:
                print("\nATENÇÃO! Esta posição do tabuleiro já está ocupada. Escolha outra posição no tabuleiro.")
                time.sleep(3)
                self.limpar_tela()
                continue

            if all(item is not None for item in self.tabuleiro):
                self.imprimir_tabuleiro()
                print("O jogo terminou em empate!")
                break

            while True:
                indice_comp = random.randint(0, 8)
                if self.tabuleiro[indice_comp] is None:
                    self.tabuleiro[indice_comp] = self.oponente
                    break

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
