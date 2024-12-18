# Constants for directions
RIGHT, DOWN, LEFT, UP = range(4)
DIRS = {RIGHT: (1, 0), DOWN: (0, 1), LEFT: (-1, 0), UP: (0, -1)}

# Function to find the starting position of the guard
def find_start(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "^":
                return x, y
    assert False, "no guard (^) in grid"

# Function to simulate the guard's patrol
def simulate(grid, x, y):
    width, height = len(grid[0]), len(grid)
    dir = UP
    visited = set([(x, y, dir)])
    while True:
        dx, dy = DIRS[dir]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < width and 0 <= ny < height):
            return {(x, y) for x, y, _ in visited}
        if grid[ny][nx] == "#":
            dir = (dir + 1) % 4
        else:
            x, y = nx, ny
            if (x, y, dir) in visited:
                return None
            visited.add((x, y, dir))

# Example data directly included in the script as a string
example_data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# Function to convert the string input into the grid format
def string_to_grid(data):
    lines = data.strip().split("\n")
    return [list(line) for line in lines]

# Convert the string data into a grid
grid = string_to_grid(example_data)

# Find the starting position of the guard
x, y = find_start(grid)

# Simulate the guard's patrol to find all visited positions (Part 1)
visited = simulate(grid, x, y)
assert visited is not None
print("Part 1:", len(visited))

# Find the number of positions where adding an obstruction causes a loop (Part 2)
part2 = 0
for bx, by in visited:
    if grid[by][bx] == "^":
        continue
    grid[by][bx] = "#"
    if simulate(grid, x, y) is None:
        part2 += 1
    grid[by][bx] = "."
print("Part 2:", part2)
