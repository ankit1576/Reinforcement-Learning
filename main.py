import tkinter as tk
import time
import numpy as np
import random

# Parameters for Q-learning
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000  # Number of training episodes


class CarGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=900, height=400, bg="white")
        self.canvas.pack()

        # Create the car and hospital on the canvas
        self.car = self.canvas.create_oval(30, 290, 80, 340, fill="red")
        self.hospital = self.canvas.create_rectangle(850, 50, 900, 100, fill="blue")
        self.canvas.create_text(875, 75, text="Hospital", fill="white")

        # Define the coordinates for each route
        self.routes = [
            [(50, 320), (150, 320), (150, 200), (300, 200), (300, 100), (850, 100)],  # Route 1
            [(50, 320), (200, 320), (200, 250), (400, 250), (400, 100), (850, 100)],  # Route 2
            [(50, 320), (250, 320), (250, 200), (500, 200), (500, 100), (850, 100)],  # Route 3
            [(50, 320), (300, 320), (300, 250), (600, 250), (600, 100), (850, 100)],  # Route 4
            [(50, 320), (350, 320), (350, 200), (700, 200), (700, 100), (850, 100)],  # Route 5
            [(50, 320), (400, 320), (400, 250), (800, 250), (800, 100), (850, 100)],  # Route 6
            [(50, 320), (450, 320), (450, 300), (850, 300), (850, 100)],  # Route 7
        ]
        # Draw the routes on the canvas
        self.draw_routes()

        # Initialize Q-table with zeros
        self.q_table = np.zeros((len(self.routes), 2))  # 2 actions: Move forward or Stay

    def draw_routes(self):
        # Draw each route with different colors and labels along the path
        route_colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'pink']  # Different colors for routes
        for i, route in enumerate(self.routes):
            for j in range(len(route) - 1):
                self.canvas.create_line(
                    route[j][0], route[j][1], route[j + 1][0], route[j + 1][1],
                    fill=route_colors[i], width=3  # Thicker lines and color distinction
                )
            # Label each route at the starting point and along the route
            self.canvas.create_text(route[0][0] + 20, route[0][1] - 20, text=f"Route {i + 1}",
                                    fill=route_colors[i], font=("Helvetica", 12, 'bold'))

            # Optionally, place a label in the middle of the route for more clarity
            mid_point = len(route) // 2
            self.canvas.create_text(route[mid_point][0] + 20, route[mid_point][1] - 20,
                                    text=f"Route {i + 1} Mid", fill=route_colors[i], font=("Helvetica", 10))

    def reset_car(self):
        # Reset car position to the starting point
        self.canvas.coords(self.car, 30, 290, 80, 340)
        self.canvas.update()

    def display_best_route(self, route_index):
        # Display the car moving along the best route
        route = self.routes[route_index]
        for position in route:
            self.canvas.coords(
                self.car, position[0] - 25, position[1] - 25, position[0] + 25, position[1] + 25
            )
            self.canvas.update()
            time.sleep(0.1)

    def train_agent(self):
        for episode in range(episodes):
            route_index = random.randint(0, len(self.routes) - 1)
            print(f"Attempt {episode + 1} with Route {route_index + 1}")

            # Initialize state and cumulative reward
            state = route_index
            total_reward = 0

            for _ in range(len(self.routes[route_index])):
                # Choose action: Explore or Exploit
                if random.uniform(0, 1) < epsilon:
                    action = random.choice([0, 1])  # 0 = Stay, 1 = Move Forward
                else:
                    action = np.argmax(self.q_table[state])

                # Take action and get reward
                if action == 1:  # Move Forward
                    reward = 10 if route_index == 4 else -1  # Assign high reward for optimal route (route 5)
                    next_state = route_index
                else:
                    reward = -1  # Penalty for staying
                    next_state = state

                # Update Q-value
                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])
                new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
                self.q_table[state, action] = new_value

                # Update state and total reward
                state = next_state
                total_reward += reward

            if route_index == 4:
                print(f"Best route is: Route {route_index + 1}")
                break
            else:
                best_route = np.argmax(np.max(self.q_table, axis=1))
                self.display_best_route(best_route)  # Track the best route found

    def run(self):
        # Train the agent and display the best route
        self.train_agent()
        best_route = np.argmax(np.max(self.q_table, axis=1))
        self.display_best_route(best_route)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reinforcement Learning Route Optimization")
    game = CarGame(root)
    game.run()
    root.mainloop()
