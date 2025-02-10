import inspect
import os
import random
from agent.classic_agent import classic_agent as Agent


def my_agent(obs, config):

    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if Agent.check_winning_move(obs, config, col, piece=1):
            return col
    for col in valid_moves:
        if Agent.check_winning_move(obs, config, col, piece=2):
            return col
    return random.choice(valid_moves)


def render_game(env, agent1, agent2):
    env.run([agent1, agent2])
    env.render(mode="ipython")


def test_my_agent(my_agent):
    # will work on kaggle
    from kaggle_environments import env
    env = make("connectx", debug=True)
    render_game(env, my_agent, "random")


def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)


if __name__ == '__main__':
    test_my_agent(my_agent)
    write_agent_to_file(my_agent, "my_agent.py")
