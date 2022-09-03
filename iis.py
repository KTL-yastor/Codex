

class GameOfLife:
    def __init__(self, size, seed):
        self.size = size
        self.seed = seed
        self.board = self.create_board()
        self.next_board = self.create_board()
        self.seed_board()

    def create_board(self):
        return [[0 for i in range(self.size)] for j in range(self.size)]

    def seed_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.seed[i][j] == 1:
                    self.board[i][j] = 1

    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0:
                    continue
                if i >= self.size or j >= self.size:
                    continue
                neighbors.append(self.board[i][j])
        return neighbors

    def get_next_state(self, x, y):
        neighbors = self.get_neighbors(x, y)
        if self.board[x][y] == 1:
            if neighbors.count(1) < 2:
                return 0
            elif neighbors.count(1) > 3:
                return 0
            else:
                return 1
        else:
            if neighbors.count(1) == 3:
                return 1
            else:
                return 0

    def update_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.next_board[i][j] = self.get_next_state(i, j)
        self.board = self.next_board
        self.next_board = self.create_board()

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=' ')
            print()
        print()


if __name__ == '__main__':
    seed = [[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]
    game = GameOfLife(5, seed)
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()
    game.print_board()
    game.update_board()