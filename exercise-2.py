def index_power(numbers, n):
    return numbers[n] ** n if n < len(numbers) else -1 
    
# print(index_power([1,3 ,10,100], 3)) 
# print(index_power([1,2,3,4], 2))
# print(index_power([1,2], 3))