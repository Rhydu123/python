import re

def extract_numbers(text):
    number_pattern = r'\d+'
    numbers = re.findall(number_pattern, text)
    return numbers

text = "The price of the product is $25.99, and the quantity is 10. Please call 555-123-4567."

numbers = extract_numbers(text)

for number in numbers:
    print(number)

