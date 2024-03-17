def chunking_by(numbers, chunck):
    #Checking if there still element in list number
    result = []
    x = 0
    temp_list = []
    for y in numbers:
        if x == chunck:
            result.append(temp_list)
            temp_list = []
            #append the current element into the new list
            temp_list.append(y)
            #as append a new element into a new list, we start counting with one
            x = 1
        else:
            temp_list.append(y)
            x += 1
    #The last list append into the result
    result.append(temp_list)
    return result

    
print(chunking_by([3, 4, 5], 1))