import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Constantes da tela
LARGURA = 600
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Tamanho dos blocos
TAMANHO_BLOCO = 20

# Relógio e velocidade
clock = pygame.time.Clock()
velocidade = 10  # FPS (velocidade da cobra)

# Função para gerar posição aleatória da comida
def gerar_fruta():
    x = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    y = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    return [x, y]

# Inicialização da cobra e da fruta
cobra = [[100, 100]]
direcao = 'DIREITA'
fruta = gerar_fruta()
pontuacao = 0

# Função para desenhar a cobra
def desenhar_cobra():
    for segmento in cobra:
        pygame.draw.rect(TELA, VERDE, pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

# Função para mostrar a pontuação
def mostrar_pontuacao():
    fonte = pygame.font.SysFont('arial', 24)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, VERMELHO)
    TELA.blit(texto, (10, 10))

# Loop principal do jogo
while True:
    clock.tick(velocidade)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != 'BAIXO':
                direcao = 'CIMA'
            elif evento.key == pygame.K_DOWN and direcao != 'CIMA':
                direcao = 'BAIXO'
            elif evento.key == pygame.K_LEFT and direcao != 'DIREITA':
                direcao = 'ESQUERDA'
            elif evento.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                direcao = 'DIREITA'

    # Mover a cobra
    x, y = cobra[0]
    if direcao == 'CIMA':
        y -= TAMANHO_BLOCO
    elif direcao == 'BAIXO':
        y += TAMANHO_BLOCO
    elif direcao == 'ESQUERDA':
        x -= TAMANHO_BLOCO
    elif direcao == 'DIREITA':
        x += TAMANHO_BLOCO

    nova_cabeca = [x, y]
    cobra.insert(0, nova_cabeca)

    # Verificar se comeu a fruta
    if nova_cabeca == fruta:
        pontuacao += 1
        fruta = gerar_fruta()
    else:
        cobra.pop()  # remove o último segmento se não comeu fruta

    # Verificar colisão com paredes
    if (x < 0 or x >= LARGURA or y < 0 or y >= ALTURA):
        break  # fim de jogo

    # Verificar colisão com o próprio corpo
    if nova_cabeca in cobra[1:]:
        break  # fim de jogo

    # Desenhar tudo
    TELA.fill(PRETO)
    desenhar_cobra()
    pygame.draw.rect(TELA, VERMELHO, pygame.Rect(fruta[0], fruta[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
    mostrar_pontuacao()
    pygame.display.flip()

# Fim de jogo
pygame.quit()
print(f"Fim de jogo! Sua pontuação foi: {pontuacao}")
