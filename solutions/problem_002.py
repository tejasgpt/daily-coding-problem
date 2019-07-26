def get_factors(array):
    factor = [0] * len(array)
    factor[0] = 1
    
    for i in range(1,len(array)):
        factor[i] = array[i-1] * factor[i-1]
        
    base = 1
    
    for j in range(len(array)-1,-1,-1):
        factor[j] *= base
        base *= array[j]
    
    return factor


assert get_factors([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert get_factors([3, 2, 1]) == [2, 3, 6]
