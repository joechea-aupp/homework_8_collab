def chunking_by(numbers, chunck):
    
    # create a list to store the result
    chuck_result = []
    
    # loop number in range from 0 to allnumbers with step
    for index in range(0, len(numbers), chunck):
        
        # in numbers take first index + step
        chuck = numbers[index:index + chunck]  
        chuck_result.append(chuck)
        
    return chuck_result


            
        
