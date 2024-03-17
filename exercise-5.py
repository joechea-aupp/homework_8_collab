def reverse_ascending(numbers):
    result = []
    subsequence = []
    
    for num in numbers:
        # if list is empty just append, if num is larger than last element also append
        if not subsequence or num > subsequence[-1]:
            subsequence.append(num)

        # if num does not extend "subsequence" then reverse the sequence but make it the result now     
        else:
            
            result.extend(reversed(subsequence))
            #start new sequence withc current num
            subsequence = [num]
    
    result.extend(reversed(subsequence))
    return result



# Test 
print(reverse_ascending([8, 9, 217, 335, 651, 4, 7, 8]))