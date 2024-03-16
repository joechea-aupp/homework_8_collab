def replace_last(numbers):
    ...
     # Check the length of the list 
    if len(numbers) <= 1:       # if length 'numbers' is less than or equal to 1: list = empty or list has only one element
        return numbers      # Return the list as it is
    else:
        return [numbers[-1]] + numbers[:-1] # Take last element to a new list, then take all element of origin list except the last one

print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))