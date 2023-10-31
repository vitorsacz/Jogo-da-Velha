import funcoes


cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
cor_azul = '\033[94m'
cor_reset = '\033[0m'  # Reseta a cor para a padrão

def main():

    op = funcoes.cabecalho()

    if (op == "S") or (op == "s") or (op == "Sim") or (op == "sim"):
        while True:
            funcoes.explicacao_game()
            
            break
    else:
        print("Obrigado por participar conosco")
        

    

if __name__ == "__main__":
    main()
