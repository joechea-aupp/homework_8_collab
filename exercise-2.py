def index_power(numbers, n):
    if n < 0 or n >= len(numbers):
        return -1
    else:
        return numbers[n]**n

print("Let's find the N-th power of the element in the array with the index N!")
input_list_str = input("Enter an array of numbers (e.g, 1,2,3):")
input_list = [int(num) for num in input_list_str.split(',')]
input_N = eval(input("Enter a number: "))

result = index_power(input_list, input_N)
print(f"Output: {result}")