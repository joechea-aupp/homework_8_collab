def index_power(numnbers, n):
    ...
    result = 0
    #condition if n is outside array of numnbers
    if n >= len(numnbers):
            result -= 1
    
    if n in numnbers:
        #caculate if n is inside array of numnbers
        result = numnbers[n] ** n 

    return result

print( index_power([1, 2, 3, 4], 2) )
print(index_power([1, 3, 10, 100], 3)) 
print( index_power([0, 1], 0) )
print( index_power([1, 2], 3) )


