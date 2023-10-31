from random import randint


def limparTela():
    print('\n'*100)
    
def cabecalho():
    print('{:^50}'.format('=' * 50))
    print('{:^50}'.format('JOGO DA VELHA'))
    print('{:^50}'.format('=' * 50))
    
def boasvindas():
    limparTela()
    cabecalho()
    print('{:^50}'.format('Bem-vindo ao jogo da velha!!'))
    print('{:^50}'.format('-' * 50))
    
def placar(nomeP1, vitoriasP1, nomeP2, vitoraP2, empates, simboloP1):
    limpar()
    cabecalho()
    if simboloP1 == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif simboloP1 == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'
    print(' '*9, f'{nomeP1[0:15]:.<15}({simboloP1}): {vitoriasP1} vitórias')
    print(' '*9, f'{nomeP2[0:15]:.<15}({simboloP2}): {vitoriasP2} vitórias')
    print(' '*9, f'                    {empates} empates')
    print('{:^50}'.format('=' * 50))
    
def tabuleiro (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print('{:^19}'.format('MAPA DO JOGO'), '          ', '{:^19}'.format('JOGO EM ANDAMENTO'))
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  1  │  2  │  3  │', '          ', f'│  {c1}  │  {c2}  │  {c3}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  4  │  5  │  6  │', '          ', f'│  {c4}  │  {c5}  │  {c6}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  7  │  8  │  9  │', '          ', f'│  {c7}  │  {c8}  │  {c9}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print()
    print(f('=' * 50))

def opcaoInicial():
    while True:
        boasvindas()
        print('Escolha...\n'
              '[0] para conhecer as regras\n'
              '[1] para ser " o "\n'
              '[2] para ser " x "\n')
        opcao = input('Qual a sua opção? ').strip()
        while opcao != '0' and opcao != '1' and opcao != '2':
            opcao = input('Opção inválida. Qual a sua opção? [0/1/2] ').strip()
            if opcao == '0':
                regras()
            if opcao == '1' or opcao == '2':
                break
            return opcao
        
def verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    
    if c1 == c2 and c1 == c3 and c1 != ' ':
        return True
    elif c4 == c5 and c4 == c6 and c4 != ' ':
        return True
    elif c7 == c8 and c7 == c9 and c7 != ' ':
        return True
    #COLUNAS
    elif c1 == c4 and c1 == c7 and c1 != ' ':
        return True
    elif c2 == c5 and c2 == c8 and c2 != ' ':
        return True
    elif c3 == c6 and c3 == c9 and c3 != ' ':
        return True
    #DIAGONAIS
    elif c1 == c5 and c3 == c7 and c3 != ' ':
        return True
    else:
        return False
    
    
