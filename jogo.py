import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import randint
HEIGHT = 400
WIDTH = 300

BLUE = 255, 0, 0
RED = 0, 0, 255
GREEN = 0, 255, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0

POS_START = [(50, 110), (110, 110), (210, 110),
             (50, 160), (110, 160), (210, 160),
             (50, 260), (110, 260), (210, 260)
             ]

POS_END = [(90, 140), (190, 140), (250, 140),
           (90, 240), (190, 240), (250, 240),
           (90, 290), (190, 290), (250, 290)
           ]


def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def table(img, start, end, color=BLACK, thickness=5):
    cv2.line(img,
             start,
             end,
             color,
             thickness)


def drawRectangle(img, start, end, color, thickness=-1):
    cv2.rectangle(img,
                  start,
                  end,
                  color,
                  thickness
                  )


def drawTriangle(img, pos, color):
    start_x, start_y = POS_START[pos]
    end_x, end_y = POS_END[pos]
    print((start_x, start_y), (end_x, start_y), ((start_x + end_x) / 2), end_y)
    vertices = np.array([[(start_x, start_y), (end_x, start_y), ((start_x + end_x) / 2, end_y)]], np.int32)
    # para o metodo fillpolly é preciso uma matriz 3D q se resolve colocando um colchete a mais no np.array
    cv2.fillPoly(img,
                 vertices,
                 color)

vazio = 0
humano = 1
cpu = 2

def check(board):
    # vitorias por linha
    if board[0] == board[1] == board[2] != vazio:
        return board[0]
    if board[3] ==board[4] == board[5] != vazio:
        return board[3]
    if board[6] == board[7] == board[8] != vazio:
        return board[6]
    # vitorias por coluna
    if board[0] == board[3] == board[6] != vazio:
        return board[0]
    if board[1] == board[4] == board[7] != vazio:
        return board[1]
    if board[2] == board[5] == board[8] != vazio:
        return board[2]
    # vitorias por diagonal
    if board[0] == board[4] == board[8] != vazio:
        return board[0]
    if board[2] == board[4] == board[6] != vazio:
        return board[2]


def main():
    image = np.empty([HEIGHT, WIDTH, 3], dtype=np.uint8)
    image.fill(255)

    table(image, (100, 100), (100, 300))
    table(image, (200, 100), (200, 300))
    table(image, (50, 150), (250, 150))
    table(image, (50, 250), (250, 250))
    current_pos = 0
    current_match = image.copy()


    occupied_position = [vazio, vazio, vazio,
                         vazio, vazio, vazio,
                         vazio, vazio, vazio
                         ]

    turno = humano
    jogadas = 0
    while 1:
        showImage(current_match)
        if turno == humano:
            print('Turno do Humano')
            pos = int(input("Informe a posicao da sua jogada: ")) - 1
            while occupied_position[pos] != vazio:
                print('Posicao ocupada. \n')
                pos = int(input("Informe a posicao da sua jogada: ")) - 1
            occupied_position[pos] = humano
            drawTriangle(current_match, pos, RED)

            jogadas += 1
            turno = cpu

        elif turno == cpu:
            print('Turno da CPU')
            pos = randint(0, 8)

            while occupied_position[pos] != vazio:

                pos = randint(0, 8)

            occupied_position[pos] = cpu

            print(pos)
            drawRectangle(current_match, POS_START[pos], POS_END[pos], BLUE)
            jogadas += 1
            turno = humano

        if jogadas == 9:
            print('EMPATE')
            break

        if check(occupied_position) == 'cpu':
            print("VITORIA DA CPU")
            break

        if check(occupied_position) == 'humano':
            print("VITORIA HUMANO")
            break

    # drawRectangle(current_match, POS_START[current_pos], POS_END[current_pos], RED)
    # drawTriangle(current_match, 5, BLUE)


main()
