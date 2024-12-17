# example data
data = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

# Split the data into lines
lines = data.strip().split('\n')

# Initialize lists to store each column
list1 = []
list2 = []

# Process each line
for line in lines:
    # Split each line by whitespace to separate columns
    col1, col2 = line.split()
    # Convert the columns to integers and append to respective lists
    list1.append(int(col1))
    list2.append(int(col2))

def compare_lists(list1, list2):
    list1.sort()
    list2.sort()

    difference = 0
    min_length = min(len(list1), len(list2))
    
    for item in range(min_length):
        difference += abs(list1[item] - list2[item])
    return difference

def calculate_similarity_score(list1, list2):
    frequency = {}
    similarity_score = 0
    
    # Count occurrences of each item in list2
    for item in list2:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    # Calculate the similarity score
    for item in list1:
        if item in frequency:
            similarity_score += item * frequency[item]
    
    return similarity_score


print(compare_lists(list1, list2))
print(calculate_similarity_score(list1, list2))



