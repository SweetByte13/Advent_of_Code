def string_to_puzzle_input(data_string):
    # Split the string by newline characters to get each row
    puzzle_input = data_string.strip().split('\n')
    return puzzle_input

data_string = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def find_xmas_pattern(grid):
    def is_xmas_pattern(x, y):
        diagonal1 = [(x-1, y-1), (x, y), (x+1, y+1)]
        diagonal2 = [(x-1, y+1), (x, y), (x+1, y-1)]
        
        def check_diagonal(diagonal):
            chars = [grid[px][py] for px, py in diagonal if 0 <= px < len(grid) and 0 <= py < len(grid[0])]
            return ''.join(chars) == "MAS" or ''.join(chars) == "SAM"
        
        return check_diagonal(diagonal1) and check_diagonal(diagonal2)

    xmas_count = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 'A' and is_xmas_pattern(i, j):
                xmas_count += 1
    
    return xmas_count

puzzle_input = string_to_puzzle_input(data_string)
print(find_xmas_pattern(puzzle_input))


