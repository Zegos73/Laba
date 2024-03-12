import re
def find_and_process(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    print("Объекты из файла:")
    print(data)
    pattern = re.findall(r'\b12\d\b', data)
    odd_numbers = [int(num) for num in pattern if int(num) % 2 != 0]
    count = len(odd_numbers)
    product = 1
    for num in odd_numbers:
        product *= num
    print(f"Количество натуральных нечетных трехразрядных чисел, где первые две цифры равны 12: {count}")
    print(f"Произведение этих чисел: {product}")
file_name = "input.txt" 
find_and_process(file_name)
