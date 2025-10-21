import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Plataforma 2D com Plataformas Suspensas")

# Cores
BRANCO = (255, 255, 255)
AZUL = (50, 150, 255)
VERDE = (0, 200, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Jogador
jogador_largura = 50
jogador_altura = 60
jogador_x = 100
jogador_y = ALTURA - jogador_altura - 100
velocidade_x = 5
velocidade_y = 0
gravidade = 0.8
forca_pulo = -15
no_chao = False

# Plataformas
plataformas = [
    pygame.Rect(0, ALTURA - 40, LARGURA, 40),      # chão
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(400, 350, 150, 20),
    pygame.Rect(600, 250, 120, 20)
]

# Loop principal
while True:
    clock.tick(FPS)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade_x
    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade_x
    if teclas[pygame.K_SPACE] and no_chao:
        velocidade_y = forca_pulo
        no_chao = False

    # Gravidade
    velocidade_y += gravidade
    jogador_y += velocidade_y

    # Cria o retângulo do jogador com posição arredondada
    jogador = pygame.Rect(round(jogador_x), round(jogador_y), jogador_largura, jogador_altura)

    # Verificar colisão com plataformas
    no_chao = False
    for plataforma in plataformas:
        if jogador.colliderect(plataforma):
            if velocidade_y > 0 and jogador.bottom <= plataforma.bottom:
                jogador_y = plataforma.top - jogador_altura
                velocidade_y = 0
                no_chao = True
                break  # para na primeira colisão detectada

    # Desenhar a tela
    TELA.fill(BRANCO)

    # Desenhar plataformas
    for plataforma in plataformas:
        pygame.draw.rect(TELA, VERDE, plataforma)

    # Desenhar jogador
    pygame.draw.rect(TELA, AZUL, jogador)

    # Atualizar a tela
    pygame.display.flip()
