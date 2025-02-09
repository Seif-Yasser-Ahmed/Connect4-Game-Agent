import numpy as np
import random
from agent import Agent


class Heuristic(Agent):
    @staticmethod
    def get_heuristic(grid, mark, config):
        num_twos = Agent.count_windows(grid, 2, mark, config)
        num_threes = Agent.count_windows(grid, 3, mark, config)
        num_fours = Agent.count_windows(grid, 4, mark, config)
        num_twos_opp = Agent.count_windows(grid, 2, mark % 2+1, config)
        num_threes_opp = Agent.count_windows(grid, 3, mark % 2+1, config)
        score = Agent.A*num_fours + Agent.B*num_threes + Agent.C * \
            num_twos + Agent.D*num_twos_opp + Agent.E*num_threes_opp
        return score

    @staticmethod
    def get_scores(obs, config, valid_moves, grid):
        return dict(zip(valid_moves, [Agent.score_move(grid, col, obs.mark, config) for col in valid_moves]))

    @staticmethod
    def my_agent(obs, config):
        valid_moves = [c for c in range(config.columns) if obs.board[c] == 0]
        grid = np.asarray(obs.board).reshape(config.rows, config.columns)

        scores = Agent.get_scores(obs, config, valid_moves, grid)
        max_cols = [key for key in scores.keys() if scores[key] ==
                    max(scores.values())]
        return random.choice(max_cols)
