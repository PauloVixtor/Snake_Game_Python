import pygame # importa o pygame
from pygame.locals import *
from sys import exit
from random import randint # gera aleatoriamente

pygame.init() # chama tudo no pygame

### Adiconando musica ao game ###
pygame.mixer.music.set_volume(0.1) # volume da musica
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Mission.mp3') # encontrar a musica nos arquivos
pygame.mixer.music.play(-1) # como tocar a musica no jogo


### Adiconando musica de colisao ###
barulho_colisao = pygame.mixer.Sound('smw_coin.wav') # musica de colisão, sempre que for colcoar um som no jogo essa deve ser a extensão para não ocorrer um erro.
barulho_colisao.set_volume(0.2)


### posição da cobra inicial ###

largura = 640
altura = 480
x_cobra = int(largura/2) # altura
y_cobra = int(altura/2) # largura

### posição cobra inicial por controle ###

velocidade = 8 # importante usar variaveis para fazer mudanças
x_controle = 20
y_controle = 20

### posição da maça inicial ###

x_maca = randint(40, 600)
y_maca = randint(50, 430)
pontos = 0 # cria a variavel pontos, para começar a pontuação
fonte = pygame.font.SysFont('Gabriola', 35, bold=True, italic=True) # cor arial, tamanho 40, negrito true, italico true.


tela = pygame.display.set_mode((largura, altura)) # cria a tela do pygame e a proporção ((tamanho x largura))
pygame.display.set_caption('Snake Game') # Adiciona o titulo a tela de display
relogio = pygame.time.Clock() # Cria um tempo, como uma taxa de fps por segundos
lista_cobra = []  # lista da posição da cobra


### comprimento inicial da cobra ###

comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo(): # reinicia o jogo e todos os parametros, essas mudanças são apenas locais, por isso, deve se chamar a função global.
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeça, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 7
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeça = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

while True:
    tela.fill((0, 0, 0))  # adicionar a cor de fundo
    for event in pygame.event.get():
        if event.type == QUIT:  # caso vc clique em fechar ele irá encerrar o jogo.
            pygame.quit()
            exit()

        # Menu do jogo
        fonte4 = pygame.font.SysFont('Gabriola', 25, True, True)
        fonte5 = pygame.font.SysFont('twcen', 80, True, italic=True) # corbel, mvboli
        titulo = 'Snake Game'
        mensagem3 = 'Inicair o jogo (Aperte Espaço)'
        mensagem4 = 'Sair ( Aperte X)'
        texto_formatado5 = fonte5.render(titulo, True, (80, 0, 200))
        texto_formatado3 = fonte4.render(mensagem3, True, (255, 255, 255))
        texto_formatado4 = fonte4.render(mensagem4, True, (255, 255, 255))
        snakegame = texto_formatado5.get_rect()
        ret_texto3 = texto_formatado3.get_rect()
        ret_texto4 = texto_formatado4.get_rect()
        snakegame.center = (largura // 2, altura // 3)
        ret_texto3.center = (largura // 2, altura // 2)
        ret_texto4.center = (largura // 2, altura // 1.5)
        tela.blit(texto_formatado5, snakegame)
        tela.blit(texto_formatado3, ret_texto3)
        tela.blit(texto_formatado4, ret_texto4)
        pygame.display.update()

        # Mensagem de iniciar o jogo

        if event.type == KEYDOWN:
            if event.key == K_x:
                pygame.quit()
                exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # pygame.mixer.music.stop()
                while True:  # Loop principall, sempre fazer isso.
                    ### Adiconando musica ao game ###
                    relogio.tick(30)  # insere a taxa de fps por segundo
                    tela.fill((255, 255, 255))  # adicionar a cor de fundo
                    mensagem = f'Pontos {pontos}'
                    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))  # texto pixelado ou não

                    for event in pygame.event.get():
                        if event.type == QUIT:  # caso vc clique em fechar ele irá encerrar o jogo.
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:  # CASO APERTE QUALQUER TECLA NO TECLADO DEVE ENTENDER ISSO
                            ### criando moviemnto continuo e sem ir para diagonal
                            if event.key == K_a:  # para esquerda
                                if x_controle == velocidade:
                                    pass  # bloqueia ou passa
                                else:
                                    x_controle = - velocidade
                                    y_controle = 0
                            if event.key == K_d:  # para direita
                                if x_controle == - velocidade:
                                    pass
                                else:
                                    x_controle = velocidade
                                    y_controle = 0
                            if event.key == K_w:  # para cima
                                if y_controle == velocidade:
                                    pass
                                else:
                                    y_controle = - velocidade
                                    x_controle = 0
                            if event.key == K_s:  # para baixo
                                if y_controle == - velocidade:
                                    pass
                                else:
                                    y_controle = velocidade
                                    x_controle = 0
                    x_cobra = x_cobra + x_controle
                    y_cobra = y_cobra + y_controle

                    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20,
                                                                 20))  # desenhar Retangulo (local, (cor), (eixo X ,Y,pixel, altura do parametro)
                    maca = pygame.draw.circle(tela, (255, 0, 0), (x_maca, y_maca), 10, 10)
                    # maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20)) # segunda imagem

                    ### Paredes ###
                    parede_dir = pygame.draw.line(tela, (0, 0, 0), (1, 0), (1, 600), 20)
                    parede_esq = pygame.draw.line(tela, (0, 0, 0), (640, 0), (640, 600), 20)
                    parede_cima = pygame.draw.line(tela, (0, 0, 0), (1, 0), (640, 0), 20)
                    parede_baixo = pygame.draw.line(tela, (0, 0, 0), (640, 480), (1, 480), 20)

                    # caso tenha abtido na esquerda
                    if cobra.colliderect(parede_esq):
                        fonte2 = pygame.font.SysFont('Gabriola', 30, True, True)
                        mensagem = 'Game Over!! Pressione "Enter" para continuar.'
                        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
                        ret_texto = texto_formatado.get_rect()
                        morreu = True
                        while morreu:
                            tela.fill((0, 0, 0))
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_KP_ENTER:
                                        reiniciar_jogo()
                            ret_texto.center = (largura // 2, altura // 2)
                            tela.blit(texto_formatado, ret_texto)
                            pygame.display.update()

                        # caso tenha batido direita
                    if cobra.colliderect(parede_dir):
                        fonte2 = pygame.font.SysFont('Gabriola', 30, True, True)
                        mensagem = 'Game Over!! Pressione "Enter" para continuar.'
                        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
                        ret_texto = texto_formatado.get_rect()
                        morreu = True
                        while morreu:
                            tela.fill((0, 0, 0))
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_KP_ENTER:
                                        reiniciar_jogo()
                            ret_texto.center = (largura // 2, altura // 2)
                            tela.blit(texto_formatado, ret_texto)
                            pygame.display.update()

                        # caso tenha batido em cima
                    if cobra.colliderect(parede_cima):
                        fonte2 = pygame.font.SysFont('Gabriola', 30, True, True)
                        mensagem = 'Game Over!! Pressione "Enter" para continuar.'
                        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
                        ret_texto = texto_formatado.get_rect()
                        morreu = True
                        while morreu:
                            tela.fill((0, 0, 0))
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_KP_ENTER:
                                        reiniciar_jogo()
                            ret_texto.center = (largura // 2, altura // 2)
                            tela.blit(texto_formatado, ret_texto)
                            pygame.display.update()

                            # Caso tenha abtido em baixo
                    if cobra.colliderect(parede_baixo):
                        fonte2 = pygame.font.SysFont('Gabriola', 30, True, True)
                        mensagem = 'Game Over!! Pressione "Enter" para continuar.'
                        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
                        ret_texto = texto_formatado.get_rect()
                        morreu = True
                        while morreu:
                            tela.fill((0, 0, 0))
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_KP_ENTER:
                                        reiniciar_jogo()
                            ret_texto.center = (largura // 2, altura // 2)
                            tela.blit(texto_formatado, ret_texto)
                            pygame.display.update()

                    if cobra.colliderect(maca):  # codigo de colisão com outro objeto
                        x_maca = randint(40, 600)  # muda posição x
                        y_maca = randint(50, 430)  # muda posição y
                        pontos = pontos + 1  # pontos a cada colisão
                        barulho_colisao.play()  # para tocar o som da colisao
                        comprimento_inicial = comprimento_inicial + 1

                    lista_cabeça = []  # cria uma lista dos movimentos
                    lista_cabeça.append(x_cobra)  # insere y na lista
                    lista_cabeça.append(y_cobra)  # insere x na lista

                    lista_cobra.append(lista_cabeça)  # que deixa apenas ultima posição
                    if lista_cobra.count(lista_cabeça) > 1:
                        fonte2 = pygame.font.SysFont('Gabriola', 30, True, True)
                        mensagem = 'Game Over!! Pressione "Enter" para continuar.'
                        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
                        ret_texto = texto_formatado.get_rect()

                        morreu = True
                        while morreu:
                            tela.fill((0, 0, 0))
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_KP_ENTER:
                                        reiniciar_jogo()

                            ret_texto.center = (largura // 2, altura // 2)
                            tela.blit(texto_formatado, ret_texto)
                            pygame.display.update()
                    if x_cobra > largura:
                        x_cobra = 0
                    if x_cobra < 0:
                        x_cobra = largura
                    if y_cobra < 0:
                        y_cobra = altura
                    if y_cobra > altura:
                        y_cobra = 0

                    if len(lista_cobra) > comprimento_inicial:  # Se o compriemnto total da cobra for maior que o que ela tem apague o ultimo
                        del lista_cobra[0]

                    aumenta_cobra(lista_cobra)  # aumenta a cobra

                    tela.blit(texto_formatado, (450, 40))  # como fazer a mensagem de pontuação aparecer na tela

                    pygame.display.update()  # vai fazer o update das informações como movimento ou outras ações.

    """
    if pygame.key.get_pressed()[K_a]: # para esquerda continuo
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]: # para direita continuod
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]: # para cima continuo
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]: # para baixo continuo
        y_cobra = y_cobra + 20
    # Testes para utilizar no jogo

    # pygame.font.get_fonts() puxa os tipos de fontes.
    # print('colidiu') # teste para ver se colidiu
    # Essa parte e um teste para  ver a movimentação do objeto na tela
    # if y >= altura:
    #     y = 0
    # y = y + 1 # altura + 1
    # pygame.draw.circle(tela, (0,0,255), (300, 260), 40) # Desenhar circulo (local, (cor), (eixo X ,Y),pixel)
    # pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5) # Desenhar linha (local, (cor), (eixo X ,Y), (eixo X ,Y) , espessura)


    ##### Referencias #####
    # link para baixar musicas free: https://freemusicarchive.org/music/BoxCat_Games
    # link para baixar o som de colisão: https://themushroomkingdom.net/media/smw/wav
    """