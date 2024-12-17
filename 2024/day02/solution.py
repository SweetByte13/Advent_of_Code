def format_data(raw_data):
    # Split the raw data into lines
    lines = raw_data.strip().split('\n')
    
    # Convert each line into a list of integers
    formatted_data = []
    for line in lines:
        formatted_line = list(map(int, line.split()))
        formatted_data.append(formatted_line)
    
    return formatted_data

# example data
raw_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

data = format_data(raw_data)

def find_safe_data(data):
    def is_safe(report):
        increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
        differences_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
        
        return (increasing or decreasing) and differences_valid
    
    def can_be_safe_with_removal(report):
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if is_safe(new_report):
                return True
        return False
    
    safe_count = 0
    for report in data:
        if is_safe(report) or can_be_safe_with_removal(report):
            safe_count += 1
    return safe_count

print(find_safe_data(data))

