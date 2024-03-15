def chunking_by(numbers, chunck):
    
    # For empty list    
    if len(number) == 0:
        print("The list is empty!")
        
        

    # create a list to store the result
    chuck_result = []
    
    # loop index in number range from 0 to all numbers with step
    for index in range(0, len(numbers), chunck):
        
        # create one chunk: in numbers, take first index till index + step 
        chuck = numbers[index:index + chunck]  
        chuck_result.append(chuck)
        
    return chuck_result

# for checking
number = [1, 2, 3, 4, 5]
chunk_size = 3

print(chunking_by(number, chunk_size))


            
        
