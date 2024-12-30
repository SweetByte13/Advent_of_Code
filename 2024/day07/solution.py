from itertools import product

# Example input data as a string
data = """
5000: 20 25 2 10
1452: 12 11 110
2345: 23 4 5 20
1010: 1 0 10 100
5678: 56 7 8 4
7890: 78 9 0
3000: 30 100 10
6789: 67 8 9 1
2500: 25 10 10 10
8765: 87 6 5
4321: 43 2 1 12
999: 99 9
147: 1 47 99
3030: 30 30 30
789: 78 9 10
2525: 25 25 25
123: 12 3 1
4567: 45 6 7
890: 8 90
2400: 24 100
5789: 57 8 9
3600: 36 100
1920: 19 20 0
8500: 85 0
1212: 12 12
"""

def evaluate(numbers, ops):
    val = numbers[0]
    for num, op in zip(numbers[1:], ops):
        if op == '+':
            val += num
        elif op == '*':
            val *= num
        elif op == '||':
            val = int(str(val) + str(num))
    return val

def generate_operator_combinations(length):
    return product(['+', '*', '||'], repeat=length)

def is_equation_valid(value, numbers):
    for ops in generate_operator_combinations(len(numbers) - 1):
        if evaluate(numbers, ops) == value:
            return True
    return False

def total_calibration_result(data):
    total = 0
    equations = data.strip().split('\n')
    for equation in equations:
        value, numbers = equation.split(': ')
        value = int(value)
        numbers = list(map(int, numbers.split()))
        if is_equation_valid(value, numbers):
            total += value
    return total

result = total_calibration_result(data)
print(f'Total Calibration Result: {result}')
