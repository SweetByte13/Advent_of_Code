# Advent of Code 2024 - Day 3: Mull It Over

## Problem Summary

In Day 3, we need to analyze a corrupted program memory to identify valid multiplication instructions and compute their results. The primary goal is to multiply numbers specified in the `mul(X,Y)` instructions, where X and Y are 1-3 digit numbers. Due to the corruption, the memory contains invalid characters that must be ignored.

### Part One

**Task**: 
- Scan the corrupted memory to find valid `mul(X,Y)` instructions and compute their results. Ignore invalid sequences that do not match the pattern.

**Example**:
- Given the input: `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
- Only the valid instructions are: `mul(2,4)`, `mul(3,7)`, `mul(11,8)`, and `mul(8,5)`
- The result is `2*4 + 3*7 + 11*8 + 8*5 = 161`

### Part Two

**Task**:
- Handle additional conditional statements: `do()` and `don't()`
- `do()` enables future `mul` instructions.
- `don't()` disables future `mul` instructions.
- Only the most recent `do()` or `don't()` instruction applies.
- At the beginning of the program, `mul` instructions are enabled.

**Example**:
- Given the input: `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`
- The valid enabled instructions are: `mul(2,4)` and `mul(8,5)` (because `mul(5,5)` and `mul(11,8)` are disabled by `don't()`)
- The result is `2*4 + 8*5 = 48`

## Approach

### Part One

1. **Input**: A string representing corrupted memory.
2. **Goal**: Identify and compute results of valid `mul(X,Y)` instructions.
3. **Steps**:
   - Use regular expressions to find valid `mul(X,Y)` instructions.
   - Extract numbers from these instructions.
   - Compute the product of the numbers and sum the results.

### Part Two

1. **Input**: A string representing corrupted memory with additional conditional statements.
2. **Goal**: Handle `do()` and `don't()` instructions to control the validity of subsequent `mul(X,Y)` instructions.
3. **Steps**:
   - Track the state of `mul` instructions (enabled or disabled) using the most recent `do()` or `don't()` instruction.
   - Process the memory string to find valid instructions based on the current state.
   - Compute the product of the numbers from valid `mul(X,Y)` instructions and sum the results.

## Results

- **Part One**: Identified the sum of results from valid `mul` instructions in the corrupted memory.
- **Part Two**: Included handling for `do()` and `don't()` instructions, computing the sum of results from valid enabled `mul` instructions.

This README provides an overview of the problem, the approach taken, and the results obtained, while respecting Advent of Code's guidelines. Happy coding! 😊🎄