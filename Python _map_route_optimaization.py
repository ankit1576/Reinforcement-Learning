import openrouteservice
import folium
import numpy as np
import random

# Initialize OpenRouteService client
client = openrouteservice.Client(key='5b3ce3597851110001cf6248b185d93ead8346d1adbd5587068dab38')  # Replace with your key

# Define start and end coordinates
start_coords = (80.92238882182758461, 26.83293623332243)
end_coords = (80.95041842860792, 26.914135557686038)

# Step 1: Generate multiple paths to the destination
paths = []
num_paths = 10  # Number of different paths to generate
for i in range(num_paths):
    try:
        # Generate slightly varying paths with random deviations for demonstration purposes
        random_waypoints = [
            (start_coords[0] + random.uniform(-0.01, 0.01), start_coords[1] + random.uniform(-0.01, 0.01)),
            (end_coords[0] + random.uniform(-0.01, 0.01), end_coords[1] + random.uniform(-0.01, 0.01)),
        ]
        route = client.directions(
            coordinates=[start_coords] + random_waypoints + [end_coords],
            profile='driving-car',
            format='geojson'
        )
        paths.append(route)
    except openrouteservice.exceptions.ApiError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Reinforcement Learning setup
n_paths = len(paths)  # Number of paths (states)
q_table = np.zeros((n_paths, n_paths))  # Q-table initialized

# RL Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000

# Reward structure
reward_goal = 100  # High reward for choosing the optimal path
penalty_per_move = -1  # Small penalty per action

# Store all paths explored during training
explored_paths = []

# Step 3: Train the RL agent
for episode in range(episodes):
    state = 0  # Start at the first path
    total_reward = 0
    for step in range(n_paths - 1):
        # Choose action: explore or exploit
        if random.uniform(0, 1) < epsilon:
            action = random.choice(range(n_paths))
        else:
            action = np.argmax(q_table[state])

        # Store the path the agent explored (for later visualization)
        explored_paths.append(action)

        # Reward calculation
        path_length = paths[action]['features'][0]['properties']['segments'][0]['distance']
        reward = reward_goal - path_length if action == n_paths - 1 else penalty_per_move

        # Q-table update
        old_value = q_table[state, action]
        next_state = action
        next_max = np.max(q_table[next_state])
        q_table[state, action] = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)

        state = next_state
        total_reward += reward
        if state == n_paths - 1:
            break

# Step 4: Extract the optimal path based on learned Q-table
best_path_index = np.argmax(np.sum(q_table, axis=1))  # Choose the path with the highest cumulative reward
best_path_coords = paths[best_path_index]['features'][0]['geometry']['coordinates']

# Step 5: Print all possible paths
print("All possible paths:")
for i, path in enumerate(paths):
    print(f"Path {i + 1}:")
    coordinates = path['features'][0]['geometry']['coordinates']
    for coord in coordinates:
        print(f"  {coord}")
    print("\n")

# Step 6: Visualize the paths and the optimal route on a map
map_visual = folium.Map(location=(start_coords[1], start_coords[0]), zoom_start=13)

# Add start and end markers
folium.Marker((start_coords[1], start_coords[0]), tooltip="Start", icon=folium.Icon(color="green")).add_to(map_visual)
folium.Marker((end_coords[1], end_coords[0]), tooltip="Destination", icon=folium.Icon(color="red")).add_to(map_visual)

# Plot all paths in gray
for i, path in enumerate(paths):
    path_coords = path['features'][0]['geometry']['coordinates']
    folium.PolyLine([(coord[1], coord[0]) for coord in path_coords], color="gray", weight=2, opacity=0.6).add_to(map_visual)

# Highlight the optimal path in blue (add this before highlighting explored paths)
folium.PolyLine([(coord[1], coord[0]) for coord in best_path_coords], color="blue", weight=6, opacity=1).add_to(map_visual)

# Highlight all tried paths in red
for explored_path in explored_paths:
    path_coords = paths[explored_path]['features'][0]['geometry']['coordinates']
    folium.PolyLine([(coord[1], coord[0]) for coord in path_coords], color="red", weight=2, opacity=0.6).add_to(map_visual)

# Save and show map
map_visual.save("optimal_and_explored_paths_map.html")
print("Map with all paths (optimal and explored) saved as 'optimal_and_explored_paths_map.html'.")
