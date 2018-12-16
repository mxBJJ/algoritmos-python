"""Programa para criar estrelas."""

from random import randint
from pygame import *
from sys import  exit

COR_PRETA = (255, 255, 255)


def criar_estrelas(janela, x, y, raio, largura):
    return draw.circle(janela, COR_PRETA, [x, y], raio, largura)


def tela():
    tamanho = largura, altura = 800, 600

    janela = display.set_mode(tamanho)
    display.set_caption("Criando estrelas")

    quantidade = 300
    eixoX = [randint(0, 800) for numero in range(quantidade)]
    eixoY = [randint(0, 600) for numero in range(quantidade)]

    FPS = 60

    clock = time.Clock()

    estrelas = []

    init()
    while True:
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            elif evento.type == KEYDOWN and evento.key == K_ESCAPE:
                exit()

        for cont in range(quantidade):
            estrelas.append(criar_estrelas(janela, eixoX[cont], eixoY[cont], 2, 2))

        clock.tick(FPS)
        display.update()

    quit()


if __name__ == '__main__':
    tela()
