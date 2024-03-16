def index_power(numnbers, n):
    ...
    if n < 0 or n >= len(numnbers):
        return -1
    else:
        return numnbers[n] ** n

print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100],  3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))
