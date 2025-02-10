import numpy as np
import random
from agent.agent import Agent


class MinMax(Agent):
    import numpy as np
    import random
    N_STEPS = 3

    @staticmethod
    def get_heuristic(grid, mark, config):
        num_threes = MinMax.count_windows(grid, 3, mark, config)
        num_fours = MinMax.count_windows(grid, 4, mark, config)
        num_threes_opp = MinMax.count_windows(grid, 3, mark % 2+1, config)
        num_fours_opp = MinMax.count_windows(grid, 4, mark % 2+1, config)
        score = num_threes - 1e2*num_threes_opp - 1e4*num_fours_opp + 1e6*num_fours
        return score

    @staticmethod
    def score_move(grid, col, mark, config, nsteps):
        next_grid = MinMax.drop_piece(grid, col, mark, config)
        score = MinMax.minimax(next_grid, nsteps-1, False, mark, config)
        return score

    @staticmethod
    def is_terminal_window(window, config):
        return window.count(1) == config.inarow or window.count(2) == config.inarow

    @staticmethod
    def is_terminal_node(grid, config):
        if list(grid[0, :]).count(0) == 0:
            return True
        # horizontal
        for row in range(config.rows):
            for col in range(config.columns-(config.inarow-1)):
                window = list(grid[row, col:col+config.inarow])
                if MinMax.is_terminal_window(window, config):
                    return True
        # vertical
        for row in range(config.rows-(config.inarow-1)):
            for col in range(config.columns):
                window = list(grid[row:row+config.inarow, col])
                if MinMax.is_terminal_window(window, config):
                    return True
        # positive diagonal
        for row in range(config.rows-(config.inarow-1)):
            for col in range(config.columns-(config.inarow-1)):
                window = list(
                    grid[range(row, row+config.inarow), range(col, col+config.inarow)])
                if MinMax.is_terminal_window(window, config):
                    return True
        # negative diagonal
        for row in range(config.inarow-1, config.rows):
            for col in range(config.columns-(config.inarow-1)):
                window = list(
                    grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
                if MinMax.is_terminal_window(window, config):
                    return True
        return False

    @staticmethod
    def minimax(node, depth, maximizingPlayer, mark, config):
        is_terminal = MinMax.is_terminal_node(node, config)
        valid_moves = [c for c in range(config.columns) if node[0][c] == 0]
        if depth == 0 or is_terminal:
            return MinMax.get_heuristic(node, mark, config)
        if maximizingPlayer:
            value = -np.Inf
            for col in valid_moves:
                child = MinMax.drop_piece(node, col, mark, config)
                value = max(value, MinMax.minimax(
                    child, depth-1, False, mark, config))
            return value
        else:
            value = np.Inf
            for col in valid_moves:
                child = MinMax.drop_piece(node, col, mark % 2+1, config)
                value = min(value, MinMax.minimax(
                    child, depth-1, True, mark, config))
            return value

    @staticmethod
    def my_agent(obs, config):
        valid_moves = [c for c in range(config.columns) if obs.board[c] == 0]
        grid = np.asarray(obs.board).reshape(config.rows, config.columns)
        scores = dict(zip(valid_moves, [MinMax.score_move(
            grid, col, obs.mark, config, MinMax.N_STEPS) for col in valid_moves]))
        max_cols = [key for key in scores.keys() if scores[key] ==
                    max(scores.values())]
        return random.choice(max_cols)
