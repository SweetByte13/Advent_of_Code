# Advent of Code 2024 - Day 2: Red-Nosed Reports

## Problem Summary

In Day 2, we are tasked with analyzing unusual data from the Red-Nosed reactor to determine which reports are considered safe. The safety criteria are as follows:
1. The levels in a report must either be all increasing or all decreasing.
2. Any two adjacent levels must differ by at least one and at most three.

### Part One
Determine how many reports are safe based on the above criteria.

### Part Two
The engineers introduce the Problem Dampener, which allows the safety systems to tolerate a single bad level. This means that a report can be considered safe if removing one level makes it meet the safety criteria.

## Approach

### Part One
1. **Input**: A list of reports, each containing a series of levels.
2. **Goal**: Check each report to see if it meets the safety criteria.
3. **Solution**:
   - Verify that the report is either strictly increasing or decreasing.
   - Ensure that the difference between any two adjacent levels is between 1 and 3.

### Part Two
1. **Input**: The same list of reports.
2. **Goal**: Check if removing a single level from an unsafe report can make it safe.
3. **Solution**:
   - For each report, check if it can become safe by removing one level.

## Example

Given the example input:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

### Part One
- **Safe Reports**:
  ```
  7 6 4 2 1
  1 3 6 7 9
  ```
- **Unsafe Reports**:
  ```
  1 2 7 8 9
  9 7 6 2 1
  1 3 2 4 5
  8 6 4 4 1
  ```
- Total Safe Reports: 2

### Part Two
- **Additional Safe Reports with Problem Dampener**:
  ```
  1 3 2 4 5  (Safe by removing the second level, 3)
  8 6 4 4 1  (Safe by removing the third level, 4)
  ```
- Total Safe Reports: 4

## Results

- **Part One**: Identified 2 safe reports.
- **Part Two**: With the Problem Dampener, identified 4 safe reports.

This README provides an overview of the problem, the approach taken, examples, and the solution code while respecting Advent of Code's guidelines. Happy coding! 😊🎄
