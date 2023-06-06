numbers = [1, 2, 3]

def convert_to_string(num):
    return str(num)

str_numbers = list(map(convert_to_string, numbers))

print(str_numbers)