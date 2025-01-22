# Function to create a formatted string
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

# Test format_string
formatted_string = format_string("John", 28)
print(formatted_string)  # Output: My name is John and I am 28 years old.


# Function to check if a number is greater, lesser, or equal to 10
def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

# Test conditional_check
print(conditional_check(15))  # Output: Greater
print(conditional_check(5))   # Output: Lesser
print(conditional_check(10))  # Output: Equal


# Function to calculate sum of numbers from 1 to n
def loop_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test loop_sum
print(loop_sum(5))  # Output: 15


# Function to perform operations on a list
def list_operations(numbers):
    return sum(numbers), max(numbers), min(numbers)

# Test list_operations
print(list_operations([1, 2, 3, 4, 5]))  # Output: (15, 5, 1)


# Function to find students with scores > 80
def dict_operations(students_dict):
    return [name for name, score in students_dict.items() if score > 80]

# Test dict_operations
students = {"John": 96, "Grace": 78, "Peter": 86, "Elizabeth": 80}
print(dict_operations(students))  # Output: ['John', 'Peter']


# Function to find common elements between two lists
def set_operations(list1, list2):
    return set(list1) & set(list2)

# Test set_operations
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(set_operations(list1, list2))  # Output: {4, 5}


# Function to perform arithmetic operations
def arithmetic_ops(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "Undefined (division by zero)"
    }

# Test arithmetic_ops
print(arithmetic_ops(10, 5))  # Output: {'addition': 15, 'subtraction': 5, 'multiplication': 50, 'division': 2.0}


# Function to perform logical operations
def logical_ops(x, y):
    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x,
        "not_y": not y
    }

# Test logical_ops
print(logical_ops(True, False))  # Output: {'and': False, 'or': True, 'not_x': False, 'not_y': True}


# Function to perform bitwise operations
def bitwise_ops(a, b):
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b,
        "left_shift_a": a << 1,
        "left_shift_b": b << 1,
        "right_shift_a": a >> 1,
        "right_shift_b": b >> 1
    }

# Test bitwise_ops
print(bitwise_ops(5, 3))  # Output: {'and': 1, 'or': 7, 'xor': 6, 'left_shift_a': 10, 'left_shift_b': 6, 'right_shift_a': 2, 'right_shift_b': 1}
