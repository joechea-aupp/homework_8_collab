def remove_all_after(numbers, n):
    result = []
    #check if the list is empty or the n element cant be found, return the list back
    if len(numbers) == 0 or n not in numbers:
        return numbers
    
    for num in numbers:
        if num != n:
            result.append(num)
        else:
            #if the cutting element is found, add it to the result and break the loop
            result.append(num)
            break
                
    return result
# print(remove_all_after([1, 2, 3, 4, 5], 3))

