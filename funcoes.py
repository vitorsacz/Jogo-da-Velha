
cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
cor_roxo = '\033[94m'
cor_default = '\033[0m'  # Reseta a cor para a padrão

def cabecalho():
    print("Bem-Vindo (a) ao nosso Jogo da Velha!")  
    op = input("Gostaria de se divertir conosco? S/N")
    print("\n")

    return op
    
def explicacao_game():
    print(cor_roxo + "Nosso jogo funciona da seguinte forma")
    
    inicializar_tabuleiro()

    print( cor_roxo + "Temos um tabuleiro com 9 posições.")
    print("\n")
    print( cor_roxo + "Quando for sua vez de jogar, voce indica uma a posição que gostaria de inserir o X.")
    print( cor_roxo + "Depois disso o computador fará sua jogada.")
    print("\n")
    print( cor_roxo + "Por fim o primeiro que juntas criar uma linha, coluna ou diagonal completa, vence a partida.")
    print( cor_roxo + "Caso nenhum dos dois consiga completar a linha, será declarado empate!")

def inicializar_tabuleiro():
    
    print("\n")
    print(cor_verde + f"  1 | 2 | 3 ")
    print(cor_verde + " -----------")
    print(cor_verde + f"  4 | 5 | 6 ")
    print(cor_verde + " -----------")
    print(cor_verde + f"  7 | 8 | 9 ")
    print("\n")



def exibir_tabuleiro(tabuleiro):
    pass

def fazer_jogada():
    pass


def verificar_vencedor():
    pass


def jogar_novamente():
    pass


def pula(linha):
    for i in range(linha):
        print("\n")


