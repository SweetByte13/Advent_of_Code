# create a rules dic with page ordering rule
# create variable sum = 0
# check update line by line
# as each num is seen, add it to seen dic
# check each num against rules dic key
# check value isnt in seen, then its True and move on to next num
# if all nums is True:
#   save line to new []
# if value is in seen:
#   then False and the line is False and cant be printed
# find middle num of each correct line and += to sum
# return sum


# Example data
rules_str = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""

updates_str = """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def parse_rules(rules_str):
    rules = {}
    for rule in rules_str.split('\n'):
        if rule.strip():
            x, y = rule.split('|')
            if x not in rules:
                rules[x] = []
            rules[x].append(y)
    return rules

def is_update_valid(update, rules):
    seen = set()
    for num in update:
        if num in rules:
            for must_be_after in rules[num]:
                if must_be_after in seen:
                    return False
        seen.add(num)
    return True

def calculate_sum_of_middle_pages(rules_str, updates_str):
    rules = parse_rules(rules_str)
    sum_middle_pages = 0
    
    for update_str in updates_str.split('\n'):
        if update_str.strip():
            update = update_str.split(',')
            if is_update_valid(update, rules):
                middle_index = len(update) // 2
                middle_num = int(update[middle_index])
                sum_middle_pages += middle_num
    
    return sum_middle_pages

# Calculate the sum
result = calculate_sum_of_middle_pages(rules_str, updates_str)
print("The total sum of middle numbers from valid updates is:", result)


def find_middle_page(update):
    return int(update[len(update) // 2])

def reorder_update(update, rules):
    from collections import deque

    in_degree = {page: 0 for page in update}
    graph = {page: [] for page in update}

    for u in update:
        if u in rules:
            for v in rules[u]:
                if v in in_degree:
                    graph[u].append(v)
                    in_degree[v] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    ordered = []

    while queue:
        current = queue.popleft()
        ordered.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered

def calculate_sum_of_incorrectly_ordered_pages(rules_str, updates_str):
    rules = parse_rules(rules_str)
    total_sum = 0
    
    for update_str in updates_str.strip().split('\n'):
        update = update_str.split(',')
        if not is_update_valid(update, rules):
            correct_order = reorder_update(update, rules)
            total_sum += find_middle_page(correct_order)
    return total_sum



# Calculate the sum
result = calculate_sum_of_incorrectly_ordered_pages(rules_str, updates_str)
print("The total sum of middle numbers from valid updates is:", result)
