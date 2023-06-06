numbers = [-3, 4, 20, 7, -25, 12, -8]

def is_positive(num):
    return num > 0


filtered_numbers = list(filter(is_positive, numbers))


print(f"положительные числа: {filtered_numbers}")