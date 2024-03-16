# numbers = [1, 2, 3, 4]

def replace_last(numbers):
    # check the length of list or the list is empty
    if len(numbers) < 2:
        return numbers
    
    else:
        last_element = numbers[0]
        numbers[0] = numbers[-1]
        numbers[-1] = last_element
        return numbers
    
# print(replace_last(numbers))