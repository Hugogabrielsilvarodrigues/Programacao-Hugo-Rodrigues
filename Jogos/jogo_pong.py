import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong Game")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Raquetes
raquete_largura = 10
raquete_altura = 100
raquete_velocidade = 7

# Posições iniciais
raquete1 = pygame.Rect(20, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)
raquete2 = pygame.Rect(LARGURA - 30, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)

# Bola
bola = pygame.Rect(LARGURA//2 - 10, ALTURA//2 - 10, 20, 20)
bola_vel_x = 5
bola_vel_y = 5

# Pontuação
pontos1 = 0
pontos2 = 0
fonte = pygame.font.SysFont("Arial", 36)

# Função para desenhar tudo
def desenhar_tela():
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, BRANCO, raquete1)
    pygame.draw.rect(TELA, BRANCO, raquete2)
    pygame.draw.ellipse(TELA, BRANCO, bola)
    pygame.draw.aaline(TELA, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    texto1 = fonte.render(str(pontos1), True, BRANCO)
    texto2 = fonte.render(str(pontos2), True, BRANCO)
    TELA.blit(texto1, (LARGURA//4 - texto1.get_width()//2, 20))
    TELA.blit(texto2, (3*LARGURA//4 - texto2.get_width()//2, 20))

    pygame.display.flip()

# Loop principal
while True:
    clock.tick(FPS)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1.top > 0:
        raquete1.y -= raquete_velocidade
    if teclas[pygame.K_s] and raquete1.bottom < ALTURA:
        raquete1.y += raquete_velocidade
    if teclas[pygame.K_UP] and raquete2.top > 0:
        raquete2.y -= raquete_velocidade
    if teclas[pygame.K_DOWN] and raquete2.bottom < ALTURA:
        raquete2.y += raquete_velocidade

    # Movimento da bola
    bola.x += bola_vel_x
    bola.y += bola_vel_y

    # Colisão com o topo e base
    if bola.top <= 0 or bola.bottom >= ALTURA:
        bola_vel_y *= -1

    # Colisão com as raquetes
    if bola.colliderect(raquete1) or bola.colliderect(raquete2):
        bola_vel_x *= -1

    # Pontuação
    if bola.left <= 0:
        pontos2 += 1
        bola.center = (LARGURA//2, ALTURA//2)
        bola_vel_x *= -1
    if bola.right >= LARGURA:
        pontos1 += 1
        bola.center = (LARGURA//2, ALTURA//2)
        bola_vel_x *= -1

    desenhar_tela()
