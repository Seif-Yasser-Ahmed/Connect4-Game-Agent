import numpy as np
import random
from agent.agent import Agent


class Heuristic(Agent):
    @staticmethod
    def get_heuristic(grid, mark, config):
        num_twos = Heuristic.count_windows(grid, 2, mark, config)
        num_threes = Heuristic.count_windows(grid, 3, mark, config)
        num_fours = Heuristic.count_windows(grid, 4, mark, config)
        num_twos_opp = Heuristic.count_windows(grid, 2, mark % 2+1, config)
        num_threes_opp = Heuristic.count_windows(grid, 3, mark % 2+1, config)
        score = Heuristic.A*num_fours + Heuristic.B*num_threes + Heuristic.C * \
            num_twos + Heuristic.D*num_twos_opp + Heuristic.E*num_threes_opp
        return score

    @staticmethod
    def score_move(grid, col, mark, config):
        next_grid = Agent.drop_piece(grid, col, mark, config)
        score = Heuristic.get_heuristic(next_grid, mark, config)
        return score

    @staticmethod
    def get_scores(obs, config, valid_moves, grid):
        return dict(zip(valid_moves, [Heuristic.score_move(grid, col, obs.mark, config) for col in valid_moves]))

    @staticmethod
    def my_agent(obs, config):
        valid_moves = [c for c in range(config.columns) if obs.board[c] == 0]
        grid = np.asarray(obs.board).reshape(config.rows, config.columns)

        scores = Heuristic.get_scores(obs, config, valid_moves, grid)
        max_cols = [key for key in scores.keys() if scores[key] ==
                    max(scores.values())]
        return random.choice(max_cols)
