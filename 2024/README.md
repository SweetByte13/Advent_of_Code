# Advent of Code 2024 - Day 1

## Problem Summary

On Day 1, we were tasked with helping a group of Elvish Senior Historians reconcile two lists of historically significant locations identified by unique IDs. The challenge involved:

1. **Part One**: Pairing up numbers from two lists and calculating the total distance between these pairs.
2. **Part Two**: Calculating a total similarity score by determining how often each number from the first list appears in the second list.

## Approach

### Part One
- **Input**: Two lists of location IDs.
- **Goal**: Pair up the numbers in ascending order and calculate the total distance between the pairs.
- **Solution**: 
  1. Sort both lists.
  2. Pair the smallest with the smallest, the second smallest with the second smallest, and so on.
  3. Calculate the distance for each pair and sum them up.

### Part Two
- **Input**: Two lists of location IDs.
- **Goal**: Calculate a similarity score based on the frequency of each number in the first list appearing in the second list.
- **Solution**: 
  1. For each number in the first list, count how many times it appears in the second list.
  2. Multiply the number by its frequency in the second list and add these products together to get the total similarity score.

## Example

Given the example input:

```
Left List:  [3, 4, 2, 1, 3, 3]
Right List: [4, 3, 5, 3, 9, 3]
```

### Part One
- Sorted Lists:
  ```
  Left List:  [1, 2, 3, 3, 3, 4]
  Right List: [3, 3, 3, 4, 5, 9]
  ```
- Pairs and Distances:
  ```
  (1, 3) -> 2
  (2, 3) -> 1
  (3, 3) -> 0
  (3, 4) -> 1
  (3, 5) -> 2
  (4, 9) -> 5
  ```
- Total Distance: `2 + 1 + 0 + 1 + 2 + 5 = 11`

### Part Two
- Frequency Count:
  ```
  3 -> 3 times
  4 -> 1 time
  2 -> 0 times
  1 -> 0 times
  ```
- Similarity Score: `3*3 + 4*1 + 2*0 + 1*0 + 3*3 + 3*3 = 31`
