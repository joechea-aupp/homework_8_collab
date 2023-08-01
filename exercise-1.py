def replace_last(numbers):
    if len(numbers) >= 1:
        last_element = numbers.pop()
        numbers.insert(0, last_element)
    return numbers 
    ...
