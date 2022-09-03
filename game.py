
import pygame
import random
import time

class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = self.create_board()
        self.running = True

    def create_board(self):
        board = [[0 for i in range(self.width // self.cell_size)] for j in range(self.height // self.cell_size)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = random.randint(0, 1)
        return board

    def draw_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, x, y):
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= len(self.board):
                    continue
                if y + j < 0 or y + j >= len(self.board[x]):
                    continue
                if self.board[x + i][y + j] == 1:
                    neighbours += 1
        return neighbours

    def update_board(self):
        new_board = [[0 for i in range(self.width // self.cell_size)] for j in range(self.height // self.cell_size)]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                neighbours = self.get_neighbours(i, j)
                if self.board[i][j] == 1:
                    if neighbours < 2 or neighbours > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if neighbours == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0
        self.board = new_board

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.update_board()
            pygame.display.flip()
            time.sleep(0.1)

if __name__ == '__main__':
    game = GameOfLife(1500, 800, 5)
    game.run()