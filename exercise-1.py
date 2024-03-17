def replace_last(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        last_element = numbers.pop()  
        numbers.insert(0, last_element)  
        return numbers

def main():
    try:
        number = input("Enter a list of numbers separated by coma: ")
        numbers = [int(num.strip()) for num in number.split(',')]  
        result = replace_last(numbers)
        
        print("Result:", result)
    except ValueError:
        print("Please enter integers that are separated by coma ")
print(main)
main()
    ...
