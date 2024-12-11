# Advent of Code 2024 - Day 4: Ceres Search

## Problem Summary

On Day 4, we are tasked with solving two parts of a word search puzzle to help a small Elf at the Ceres monitoring station.

### Part One

**Task**:
- Find all occurrences of the word "XMAS" in a grid of letters.
- The word can be horizontal, vertical, diagonal, written backwards, or overlapping other words.

**Example**:
Given the grid:
```
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
```
The word "XMAS" appears 18 times.

### Part Two

**Task**:
- Find all occurrences of the "X-MAS" pattern, which consists of two "MAS" sequences forming an 'X' shape.
- Each "MAS" sequence can be written forwards or backwards.

**Example**:
The pattern "X-MAS" can be identified as:
```
M.S
.A.
M.S
```
Given the same grid, the "X-MAS" pattern appears 9 times.

## Approach

### Part One

1. **Input**: A grid of letters (list of strings).
2. **Goal**: Identify and count all occurrences of "XMAS" in various directions.
3. **Steps**:
   - Use nested loops to traverse each cell in the grid.
   - Check for "XMAS" in all possible directions (horizontal, vertical, diagonal).
   - Count and sum the occurrences.

### Part Two

1. **Input**: The same grid of letters.
2. **Goal**: Identify and count all occurrences of the "X-MAS" pattern.
3. **Steps**:
   - Use nested loops to traverse each cell in the grid.
   - Check for 'A' and then verify the diagonals to identify the "X-MAS" pattern.
   - Ensure that each "MAS" sequence can be either forwards or backwards.
   - Count and sum the occurrences.

## Results

- **Part One**: Determined the total count of "XMAS" occurrences in the grid.
- **Part Two**: Included the additional complexity of finding "X-MAS" patterns and computed their total count.

This README provides an overview of the problem, the approach taken, and the results obtained while respecting Advent of Code's guidelines. Happy coding! 🎄🚀