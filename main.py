def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("---------")

def verifica_vencedor(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    # Verifica diagonais
    if (tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"

    print("Bem-vindo ao Jogo da Velha!\n")
    print_tabuleiro(tabuleiro)

    while True:
        print(f"\nVez do jogador {jogador}.")
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
        else:
            print("Posição já preenchida. Tente novamente.")
            continue

        print_tabuleiro(tabuleiro)

        # Verifica se houve um vencedor
        if verifica_vencedor(tabuleiro, jogador):
            print(f"\nJogador {jogador} venceu! Parabéns!")
            break

        # Verifica se houve empate
        if all([all([celula != " " for celula in linha]) for linha in tabuleiro]):
            print("\nEmpate!")
            break

        # Alterna o jogador
        jogador = "O" if jogador == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()
