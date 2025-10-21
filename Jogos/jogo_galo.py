import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Tela
LARGURA = 600
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha (Galo)")

# Grade
TAMANHO_CELULA = LARGURA // 3
linha_largura = 10

# Estado do jogo
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
jogo_encerrado = False
vencedor = None

# Fonte
fonte = pygame.font.SysFont("Arial", 80)
fonte_final = pygame.font.SysFont("Arial", 50)

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    TELA.fill(BRANCO)
    
    # Linhas verticais
    pygame.draw.line(TELA, PRETO, (TAMANHO_CELULA, 0), (TAMANHO_CELULA, ALTURA), linha_largura)
    pygame.draw.line(TELA, PRETO, (2 * TAMANHO_CELULA, 0), (2 * TAMANHO_CELULA, ALTURA), linha_largura)

    # Linhas horizontais
    pygame.draw.line(TELA, PRETO, (0, TAMANHO_CELULA), (LARGURA, TAMANHO_CELULA), linha_largura)
    pygame.draw.line(TELA, PRETO, (0, 2 * TAMANHO_CELULA), (LARGURA, 2 * TAMANHO_CELULA), linha_largura)

    # Desenha os X e O
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != "":
                texto = fonte.render(tabuleiro[linha][coluna], True, AZUL if tabuleiro[linha][coluna] == "X" else VERMELHO)
                x = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2 - texto.get_width() // 2
                y = linha * TAMANHO_CELULA + TAMANHO_CELULA // 2 - texto.get_height() // 2
                TELA.blit(texto, (x, y))

    # Mensagem de fim de jogo
    if jogo_encerrado:
        texto = f"{'Empate!' if vencedor is None else f'{vencedor} venceu!'}"
        msg = fonte_final.render(texto, True, PRETO)
        TELA.blit(msg, (LARGURA // 2 - msg.get_width() // 2, ALTURA // 2 - msg.get_height() // 2))

# Verifica vitória
def checar_vencedor():
    global vencedor, jogo_encerrado

    # Linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "":
            vencedor = linha[0]
            jogo_encerrado = True
            return

    # Colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != "":
            vencedor = tabuleiro[0][col]
            jogo_encerrado = True
            return

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        vencedor = tabuleiro[0][0]
        jogo_encerrado = True
        return
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        vencedor = tabuleiro[0][2]
        jogo_encerrado = True
        return

    # Empate
    if all(cell != "" for row in tabuleiro for cell in row):
        vencedor = None
        jogo_encerrado = True

# Reiniciar o jogo
def reiniciar_jogo():
    global tabuleiro, jogador_atual, jogo_encerrado, vencedor
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_encerrado = False
    vencedor = None

# Loop principal
while True:
    desenhar_tabuleiro()
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.MOUSEBUTTONDOWN and not jogo_encerrado:
            x, y = pygame.mouse.get_pos()
            linha = y // TAMANHO_CELULA
            coluna = x // TAMANHO_CELULA

            if tabuleiro[linha][coluna] == "":
                tabuleiro[linha][coluna] = jogador_atual
                checar_vencedor()
                if not jogo_encerrado:
                    jogador_atual = "O" if jogador_atual == "X" else "X"

        elif evento.type == pygame.MOUSEBUTTONDOWN and jogo_encerrado:
            reiniciar_jogo()
