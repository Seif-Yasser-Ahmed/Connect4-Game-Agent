# Connect4-Agent
This repository contains an implementation of a Connect4 game agent using various strategies, including a classic agent, a heuristic-based one-step lookahead agent, and a minimax algorithm. The project is structured to allow easy experimentation and extension of different agent strategies.
The implemented agents include:
- A **Classic Agent** that follows a simple heuristic to make moves.
- A **Heuristic Agent** using a one-step lookahead strategy.
- A **Minimax Agent** that applies the Minimax algorithm with depth-limited search.
- An **Alpha-Beta Pruning Agent** that optimizes Minimax by pruning unnecessary branches.

These agents are designed to play the Connect4 game within the Kaggle environment.

## Key Features
- Classic Agent: A simple agent that checks for immediate winning moves and blocks the opponent's winning moves.
- Heuristic Agent: A more advanced agent that uses a heuristic function to evaluate the best move based on the current board state.
- Minimax Agent: An agent that uses the minimax algorithm with a specified depth to determine the optimal move by exploring possible future states.

## Project Structure
```
connect4-game-agent/
├── README.md
├── LICENSE
├── main.py
└── agent/
    ├── __init__.py
    ├── agent.py
    ├── classic_agent.py
    ├── heuristic.py
    ├── minmax.py
    ├── alphabeta.py
    ├── utils.py
```

### Directories and Python Classes

- **`main.py`**: The main script to test and run the agent. It includes a function to render the game and test the agent against a random opponent.
  
- **`agent/`**: Contains different agent implementations.
  - `agent.py`: Base class with utility functions for the agents like `drop_piece` and `check_window`.
  - `classic_agent.py`: Implements the classic agent that checks for immediate winning moves.
  - `heuristic.py`: Implements the heuristic-based agent that evaluates moves using a scoring function.
  - `minmax.py`: Implements the minimax agent that uses the minimax algorithm to determine the best move.
  - `utils.py`: Utility functions and configurations for the agents.
- **main.py**: Script to test and run the agent in the Kaggle environment.

## Submissions to Kaggle Competition
This repository is associated with submissions to the Kaggle competition:
- **Classic Agent Submission:** [First Submission - Play The Game](https://www.kaggle.com/code/seifyasserahmed/exercise-play-the-game)
- **Heuristic One-Step Lookahead Submission:** [Second Submission - One Step Lookahead](https://www.kaggle.com/code/seifyasserahmed/exercise-one-step-lookahead)
- **Minimax Algorithm Submission:** [Third Submission - N Step Lookahead](https://www.kaggle.com/code/seifyasserahmed/exercise-n-step-lookahead)


## Acknowledgment
Special thanks to [Alexis Cook](https://www.kaggle.com/alexisbcook) for her Kaggle course: [Intro to Game AI and Reinforcement Learning](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning), which helped and provided valuable guidance in understanding and implementing these agents.
## License
This project is licensed under the `MIT License`. See the [LICENSE](LICENSE) file for details.

---
Feel free to explore the code, experiment with different agents, and contribute to the project!
