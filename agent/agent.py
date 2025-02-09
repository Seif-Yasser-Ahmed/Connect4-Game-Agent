
class Agent:
    def __init__(self, config, obs):
        self.config = config
        self.obs = obs
        self.A = 1e6
        self.B = 1e4
        self.C = 1
        self.D = -1
        self.E = -1e4

    @staticmethod
    def drop_piece(grid, col, piece, config):
        next_grid = grid.copy()
        for row in range(config.rows-1, -1, -1):
            if next_grid[row][col] == 0:
                break
        next_grid[row][col] = piece
        return next_grid

    @staticmethod
    def check_window(window, num_discs, piece, config):
        return (window.count(piece) == num_discs and window.count(0) == config.inarow-num_discs)

    @staticmethod
    def count_windows(grid, num_discs, piece, config):
        num_windows = 0
        # horizontal
        for row in range(config.rows):
            for col in range(config.columns-(config.inarow-1)):
                window = list(grid[row, col:col+config.inarow])
                if Agent.check_window(window, num_discs, piece, config):
                    num_windows += 1
        # vertical
        for row in range(config.rows-(config.inarow-1)):
            for col in range(config.columns):
                window = list(grid[row:row+config.inarow, col])
                if Agent.check_window(window, num_discs, piece, config):
                    num_windows += 1
        # positive diagonal
        for row in range(config.rows-(config.inarow-1)):
            for col in range(config.columns-(config.inarow-1)):
                window = list(
                    grid[range(row, row+config.inarow), range(col, col+config.inarow)])
                if Agent.check_window(window, num_discs, piece, config):
                    num_windows += 1
        # negative diagonal
        for row in range(config.inarow-1, config.rows):
            for col in range(config.columns-(config.inarow-1)):
                window = list(
                    grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
                if Agent.check_window(window, num_discs, piece, config):
                    num_windows += 1
        return num_windows
