
def my_agent(obs, config):
    import random
    from utils import Agent
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
    from kaggle_environments import env
    env = make("connectx", debug=True)
    render_game(env, my_agent, "random")


if __name__ == '__main__':
    test_my_agent(my_agent)
