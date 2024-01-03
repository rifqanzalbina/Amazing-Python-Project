import random

GRID_SIZE = 20
NUM_ORGANISMS = 5
NUM_RESOURCES = 25
ENERGY_THREESHOLD = 15

RULES = {
    0 : lambda neighbors, energy : (sum(neighbors) + energy) % 2,
    1 : lambda neighbors, energy : (sum(neighbors) - energy) % 2
}

def initialize_grid():
    grid = [0] * GRID_SIZE
    for _ in range(NUM_ORGANISMS):
        organims_positions = random.randint(0, GRID_SIZE - 1)
        grid[organims_positions] = random.randint(1, 5)
    for _ in range(NUM_RESOURCES):
        resource_positions = random.randint(0, GRID_SIZE - 1)
        resource_value = random.randint(1, 5)
        grid[resource_positions] = -resource_value
    return grid

def get_neighbors(grid, index):
    neighbors = []
    if index > 0:
        neighbors.append(grid[index - 1])
    if index < GRID_SIZE - 1:
        neighbors.append(grid[index + 1])
    return neighbors

def apply_true(grid, index):
    cell_state = grid[index]
    neighbors = get_neighbors(grid, index)
    if cell_state > 0:
        energy = cell_state
        new_state = RULES[cell_state % len(RULES)](neighbors, energy)
        if energy >= ENERGY_THREESHOLD and grid.count(0) > 1:
            empty_spots = [i for i in range(GRID_SIZE) if grid[i] == 0]
            new_organism_position = random.choice(empty_spots)
            grid[new_organism_position] = energy // 2
        grid[index] = new_state
    elif cell_state < 0:
        grid[index] = 0
        
def run_simulator(grid, num_iterations):
    for _ in range(num_iterations):
        new_grid = grid.copy()
        for i in range(GRID_SIZE):
            apply_true(new_grid, i)
        grid = new_grid
    return grid

def display_grid(grid):
    for cell in grid:
        if cell == 0:
            print('.', end=' ')
        elif cell > 0:
            print(' O ', end=' ')
        else:
            print(abs(cell), end=' ') 

    print()
    
def main():
    grid = initialize_grid()
    display_grid(grid)
    
    num_iterations = 10
    grid = run_simulator(grid, num_iterations)
    
    print("\n Simulation Results : ")
    display_grid(grid)
    
if __name__ == "__main__":
    main()        