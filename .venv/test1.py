from nt import access

import pygame
import math


class Board:
    # создание поля
    def __init__(self, width, height):
        global screen
        self.width = width
        self.height = height
        self.size = self.width, self.height

        self.board = [[0] * width for _ in range(height)]
        # print(self.size)

        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.white = []

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        n = self.cell_size  # кол-ва квадратов
        for i in range(self.width):  # y
            for j in range(self.height):  # x
                pygame.draw.rect(screen, (255, 255, 255),
                                 (i * self.cell_size + self.left, j * self.cell_size + self.top, n, n), 1)

    def get_click(self, mouse_pos):
        # cell = self.get_cell(mouse_pos)
        # self.on_click(cell)
        # print(mouse_pos)
        acess = 0
        x = mouse_pos[0]
        y = mouse_pos[-1]
        all_x = self.cell_size * self.width + self.left
        all_y = self.cell_size * self.height + self.top
        if x >= self.left and x <= all_x and y >= self.top and y <= all_y:
            x_1 = abs(math.ceil((all_x - x) / self.cell_size - self.width))
            y_1 = abs(math.ceil((all_y - y) / self.cell_size - self.height))
            print(f'({x_1}, {y_1})')
        else:
            print(None)
            acess = None
        if acess != None:
            start_pos_x = x_1 * self.cell_size + self.left
            start_pos_y = y_1 * self.cell_size + self.top

            # screen.fill(pygame.Color('white'), pygame.Rect(start_pos_x, start_pos_y, self.cell_size, self.cell_size))
            count = 0
            if [start_pos_x, start_pos_y] not in self.white:
                screen.fill(pygame.Color('red'),
                            pygame.Rect(start_pos_x, start_pos_y, self.cell_size, self.cell_size))
                self.white.append([start_pos_x, start_pos_y])

            elif [start_pos_x, start_pos_y] in self.white and [start_pos_x, start_pos_y, 1] not in self.white:
                screen.fill(pygame.Color('blue'),
                            pygame.Rect(start_pos_x, start_pos_y, self.cell_size, self.cell_size))
                self.white.append([start_pos_x, start_pos_y, 1])

            else:
                screen.fill(pygame.Color('black'),
                            pygame.Rect(start_pos_x, start_pos_y, self.cell_size, self.cell_size))
                self.white.remove([start_pos_x, start_pos_y])
                self.white.remove([start_pos_x, start_pos_y, 1])

            # screen.fill(pygame.Color('white'), pygame.Rect(start_pos_x, self.top, self.cell_size, self.cell_size*self.height))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        # screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
