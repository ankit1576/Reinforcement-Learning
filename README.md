# Reinforcement-Learning
[Learn in detail from  source](https://databasetown.com/basics-of-reinforcement-learning/)

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent's goal is to maximize cumulative rewards over time by choosing actions that lead to the most favorable outcomes. 

![image](https://github.com/user-attachments/assets/a84ae863-c845-445c-884d-64064336a94c)


Here’s how it works in brief:
1. **Agent**: The learner or decision-maker.
2. **Environment**: The world in which the agent operates and makes decisions.
3. **Actions**: Choices available to the agent.
4. **Rewards**: Feedback from the environment, which can be positive or negative based on the agent’s actions.
5. **Policy**: A strategy that the agent follows to decide actions based on the current state.

The agent starts by exploring actions and receiving rewards, learning over time to improve its policy. This process uses **trial and error** to find the optimal actions that maximize long-term rewards, balancing between **exploration** (trying new actions) and **exploitation** (choosing known rewarding actions). 
![image](https://github.com/user-attachments/assets/69fed7ae-ccda-4c9e-ab9e-1228c0e64c64)

## Goal
Main is to achieve best optimal result 

Popular RL algorithms include **Q-learning**, **Deep Q-Networks (DQN)**, and **Policy Gradient** methods. RL is widely used in areas like robotics, game playing, and recommendation systems.

## Examples include
Here are a few more short examples of Reinforcement Learning:

1. **Self-Driving Cars**: A self-driving car learns to navigate roads, avoid obstacles, and follow traffic rules by receiving rewards for safe driving behaviors and penalties for errors like crossing lanes or getting too close to other vehicles.

2. **Game Playing**: In chess or Go, an AI learns by playing against itself, receiving rewards for winning moves and penalties for poor moves. Over time, it learns the strategies that maximize its chances of winning.

3. **Personalized Recommendations**: Online platforms (like Netflix or YouTube) use reinforcement learning to recommend content by tracking user interactions. If a user clicks and engages, it rewards that choice, helping refine future recommendations.

4. **Warehouse Robots**: Robots in warehouses learn the most efficient routes for picking and placing items by getting rewarded for fast, accurate deliveries and penalized for taking too long or choosing inefficient routes. 

## Markov Decision process
A **Markov Decision Process (MDP)** is a mathematical framework used for decision-making in situations where outcomes are partly random and partly under an agent's control. It consists of:
![image](https://github.com/user-attachments/assets/6c33743b-6ef8-4fb7-9da5-1745a4180771)


1. **States (S)**: All possible conditions the agent can be in.
2. **Actions (A)**: Choices available to the agent in each state.
3. **Transition Probabilities (P)**: Chances of moving from one state to another after an action.
4. **Rewards (R)**: Feedback received after each action.
complex sequential decision-making problems, especially where future outcomes depend on both the current action and state.

The goal in an MDP is to find an **optimal policy** (a strategy) that maximizes the expected cumulative reward over time, balancing immediate and future rewards.

[link to learn in deatil ](https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-markov-decision-process/)

![image](https://github.com/user-attachments/assets/8381eabd-19b8-4082-9c3e-b3efdcb81ba6)
we have used Q learning in our route optimization process so lets discuss the Q learning in depth Q leaning where Q stands for quality
## Q learning
[learn in depth](https://www.geeksforgeeks.org/q-learning-in-python/)

**Q-learning** is a type of reinforcement learning algorithm that helps an agent learn how to act optimally in a given environment by using a Q-value function. This function estimates the "quality" of taking a certain action in a specific state, helping the agent determine the best actions over time.

In Q-learning:

![image](https://github.com/user-attachments/assets/d8b67dc7-3f26-4fd0-af2b-eb3c887501cd)

Q-learning is often used for environments where the full model is unknown or complex, as it allows the agent to learn from experience without needing a predefined model of the environment.

## steps in Q learning
![image](https://github.com/user-attachments/assets/f047fd48-5523-47d2-929b-951c504ae741)


## Reinforcement Learning Route Optimization visulization


 Q-learning, a reinforcement learning algorithm, to train an agent (car) to find the optimal route to reach a destination (hospital) on a 2D grid. The agent learns to navigate a set of predefined routes, ultimately learning which route is best based on rewards received during training.


### How It Works

1. **Environment Setup**:
   - A 2D canvas is created using `Tkinter`, with a red "car" and a blue "hospital" as the destination.
   - Seven routes, each represented by a set of coordinates, are drawn on the canvas. Each route is labeled with its respective number and color for clarity.
   
![image](https://github.com/user-attachments/assets/baea6187-8f6d-4d65-8511-351d542b6da3)

2. **Q-Learning Parameters**:
   - `alpha`: Learning rate, controls how much new information overrides old information.
   - `gamma`: Discount factor, determines the importance of future rewards.
   - `epsilon`: Exploration rate, controls the balance between exploring new actions and exploiting known ones.
   - `episodes`: Number of training episodes, or rounds, the agent will run.

3. **Q-Table Initialization**:
   - A Q-table with dimensions `[number_of_routes, 2]` is created, with each route corresponding to a state, and each state having two possible actions: `0 (Stay)` and `1 (Move Forward)`.
### Explring all routes to destination

4. **Training Process**:
   - During each episode, a random route is selected, and the agent tries to navigate it.
   - At each step, the agent chooses an action based on the epsilon-greedy policy (explore or exploit).
   - Rewards are assigned:
     - `+10` for moving forward on the optimal route (Route 5).
     - `-1` for staying or moving forward on non-optimal routes.
   - Q-values are updated using the Q-learning formula:
     ![image](https://github.com/user-attachments/assets/c4e95470-62c1-409d-b9d1-b3e909fe0bcb)
   - The training loop continues until the agent consistently identifies the best route (Route 5).

6. **Displaying the Best Route**:
   - Once training completes, the car moves along the optimal route, visually demonstrating the learned path to the hospital.


https://github.com/user-attachments/assets/a2aa6c1a-9ef4-4a37-b8a2-00a932ae0268


  
# Reinforcement Learning Route Optimization in 15km Map radius
Start position: luchnow charbagh metro station
End position:Icon hospital 
![image](https://github.com/user-attachments/assets/189e4df5-e670-48af-829a-8c877565952b)
fig : showing optimal route through api to check what should be the optimal route in reinforcemnt learning

Now we are going to use Q-learning, a reinforcement learning algorithm, to help an agent (car) find the optimal route to a destination (hospital) on a map. Through trial and error, the agent learns to select the shortest, most efficient path among randomly generated alternatives.

## Project Overview

1. **Path Generation**:
   - Randomized paths between a start and end point are generated using `openrouteservice`.
   - Paths include slight deviations to simulate multiple routing options.
     ### Exploration of different paths
      ![Screenshot 2024-11-09 135403](https://github.com/user-attachments/assets/685bf70e-027e-43c8-adb7-7c5887d949c6)
     fig:Path exploration num_path=5 only
     ![Screenshot 2024-11-09 141701](https://github.com/user-attachments/assets/db53a3c4-2e91-4803-a020-e886f3e9149a)
     fig:Path exploration num_path=10 only
     ![Screenshot 2024-11-09 142755](https://github.com/user-attachments/assets/94404c50-dc7c-49a5-b00c-af4b773dcda9)
     fig:Path exploration num_path=50 only


2. **Reinforcement Learning (Q-Learning)**:
   - Q-learning is employed to teach the agent to choose the optimal route based on cumulative rewards.
   - Each path is evaluated, and the agent is rewarded or penalized based on the length and outcome of the route taken.

3. **Map Visualization**:
   - The `folium` library is used to create an interactive map.
   - All paths are displayed, with the optimal route highlighted.


## Features

- **Randomized Path Exploration**: 50 paths are created with randomized variations.
- **Reinforcement Learning-Based Optimization**: The Q-learning algorithm identifies the optimal path.
- **Interactive Map**: The final map shows all paths, highlighting the best one in blue, and marking all explored paths in red.


## How It Works

1. **Path Generation**:
   - Uses OpenRouteService API to get possible paths from start to destination.
   - Start and destination coordinates are predefined.

2. **Q-Learning Setup**:
   - Q-table is initialized to track rewards for state-action pairs.
   - Agent is trained over multiple episodes to explore and exploit paths, aiming to maximize the total reward.

3. **Optimal Path Extraction**:
   - After training, the path with the highest reward is identified as optimal and highlighted.

4. **Visualization**:
   - The final map is generated with `folium`, saving the result as `optimal_and_explored_paths_map.html`.

---

## Setup and Requirements

- **Python 3.x**
- **Libraries**:
  - `openrouteservice`: To generate directions based on OpenRouteService API.
  - `folium`: For map visualization.
  - `numpy`: For numerical operations.

Install required libraries:
```bash
pip install openrouteservice folium numpy
```

## Running the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Configure the API Key**:
   Replace the `client` initialization line in the code with your OpenRouteService API key:
   ```python
   client = openrouteservice.Client(key='YOUR_API_KEY')
   ```

3. **Run the script**:
   ```bash
   python your_script_name.py
   ```

4. **View the map**:
   Open `optimal_and_explored_paths_map.html` to view the map showing all routes and the optimal path.


### Code Execution

Run the script using Python. The `Tkinter` window will open, displaying the routes. The car will then "learn" the best route to the hospital, and ultimately follow the optimal path.


