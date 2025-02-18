import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from tqdm import tqdm  # Import tqdm for progress bar

# Define the Monopoly board (40 spaces)
BOARD_SIZE = 40

# Define the number of players and turns
NUM_PLAYERS = 4
NUM_TURNS = 100000  # Large number of turns

# Special spaces (these influence movement)
JAIL = 10
GO_TO_JAIL = 30

# Chance and Community Chest that may move the player (simplified)
CHANCE_MOVES = [0, 24, 11, 39, 5, GO_TO_JAIL]  # Possible destinations
COMMUNITY_CHEST_MOVES = [0, JAIL]  # Go to GO or Jail

# Initialize player positions
player_positions = [0] * NUM_PLAYERS
visited_spaces = []

def roll_dice():
    """Simulate rolling two dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2, die1 == die2  # Return sum and if it's a double

# Main simulation loop with a progress bar
for _ in tqdm(range(NUM_TURNS), desc="Simulating Monopoly Turns", unit="turn"):
    for player in range(NUM_PLAYERS):
        roll, is_double = roll_dice()
        new_position = (player_positions[player] + roll) % BOARD_SIZE
        player_positions[player] = new_position
        visited_spaces.append(new_position)

        # Handle special spaces
        if new_position == GO_TO_JAIL:
            player_positions[player] = JAIL  # Sent to jail
            visited_spaces.append(JAIL)

        # Simulating Chance or Community Chest (random)
        if new_position in [2, 17, 33]:  # Community Chest
            if random.random() < 0.15:  # 15% chance to move
                move_to = random.choice(COMMUNITY_CHEST_MOVES)
                player_positions[player] = move_to
                visited_spaces.append(move_to)
        
        elif new_position in [7, 22, 36]:  # Chance
            if random.random() < 0.15:  # 15% chance to move
                move_to = random.choice(CHANCE_MOVES)
                player_positions[player] = move_to
                visited_spaces.append(move_to)

# Count most visited spaces
space_counts = Counter(visited_spaces)
most_visited = space_counts.most_common(10)

# Display results
print("\nTop 10 Most Visited Spaces:")
for space, count in most_visited:
    print(f"Space {space}: {count} visits")

# Plot the most visited spaces
spaces, counts = zip(*most_visited)
plt.figure(figsize=(10, 5))
plt.bar(spaces, counts, color='blue')
plt.xlabel("Board Space")
plt.ylabel("Number of Visits")
plt.title("Most Visited Spaces in Monopoly Simulation")
plt.xticks(spaces)
plt.show()
