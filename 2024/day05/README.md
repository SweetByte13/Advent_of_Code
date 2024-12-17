# README

## Solution Overview

This repository contains a solution for two parts of a coding challenge involving page ordering and validation for safety manuals. The challenge requires checking if updates to the manuals are correctly ordered according to specific rules and then processing incorrectly-ordered updates by reordering them correctly.

### Part 1: Identify Correctly-Ordered Updates

In the first part of the challenge, the goal is to identify which updates to the safety manuals are already in the correct order according to the given rules. The steps involved are:

1. **Parse the Rules**: Convert the page ordering rules from the input string into a dictionary for easy lookup.
2. **Check Updates**: For each update, check if the pages are ordered correctly according to the rules.
3. **Calculate the Sum**: For correctly-ordered updates, find the middle page number and sum these values.

### Part 2: Fix Incorrectly-Ordered Updates

In the second part, the focus is on processing the updates that are not in the correct order. The steps involved are:

1. **Identify Incorrectly-Ordered Updates**: Use the same validation logic from Part 1 to find updates that are incorrectly ordered.
2. **Reorder Updates**: For each incorrectly-ordered update, use topological sorting to reorder the pages correctly.
3. **Calculate the Sum**: Find the middle page number of each corrected update and sum these values.

## Code Explanation

### Helper Functions

- **`parse_rules(rules_str)`**: Parses the rules from the input string and returns a dictionary where keys are page numbers and values are lists of page numbers that must come after the key page.
- **`is_update_valid(update, rules)`**: Checks if a given update is correctly ordered according to the rules.
- **`find_middle_page(update)`**: Finds the middle page number of an update.
- **`reorder_update(update, rules)`**: Reorders a given update according to the rules using topological sorting.

### Main Functions

- **`calculate_sum_of_middle_pages(rules_str, updates_str)`**: Processes the input rules and updates, checks each update for correctness, and sums the middle page numbers of correctly-ordered updates.
- **`calculate_sum_of_incorrectly_ordered_pages(rules_str, updates_str)`**: Processes the input rules and updates, identifies incorrectly-ordered updates, reorders them, and sums the middle page numbers of the reordered updates.

## Usage

You can run the provided functions with your specific rules and updates data to determine the sums of middle page numbers for both correctly-ordered and reordered updates.

## Conclusion

This solution provides a systematic approach to validating and correcting page orders based on specified rules. By following the provided functions and logic, you can easily identify and fix updates while calculating the necessary sums for the middle page numbers.