def reverse_ascending(numbers):
    ...
    # CREATE THE EMPTY LIST TO STORE THE FINAL OUTPUT
    result = []
    # CREATE NEW CURRENT ASCENDING LIST
    ascendinglist2 = []
    # USE FOR LOOP THAT ITERATE EACH NUMBERS IN INPUTS
    for num in numbers:
        # CHECK IF CURRENT NUMBERS IS SMALLER
        if ascendinglist2 and num <= ascendinglist2[-1]:
            # IF CONDITION IS TRUE, IT'S REVERSE AND ADD TO RESULT
            result.extend(reversed(ascendinglist2))
            # RESET AND READY TO START A NEW LIST
            ascendinglist2 = []
        ascendinglist2.append(num)
        # AFTER LOOP THIS LINE WILL ADD THE LAST SUBSEQUENCES TO THE RESULT
    result.extend(reversed(ascendinglist2)) 
    return result

print (reverse_ascending([1, 2, 3, 4, 5]))
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) 
print (reverse_ascending([5, 4, 3, 2, 1]))
print (reverse_ascending([]))
