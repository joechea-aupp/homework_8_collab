def remove_all_after(numbers, n):
    if n in numbers:
        # Find the index of 'n'
        n_index = numbers.index(n)
        # Return the list up to and including 'n'
        return numbers[:n_index + 1]
    else: # If 'n' is not found or the list is empty, return the original list
        return numbers
    

print(remove_all_after([1, 2, 3, 4, 5], 3)) 
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))  
print(remove_all_after([], 5))


    
