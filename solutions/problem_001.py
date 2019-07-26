def check_sums(array, k):
    if not array and not k:
        return True
    
    if not array or not k:
        return False
    
    maps = dict()
    
    for i in range(len(array)):
        if k - array[i] in maps:
            return True
        else:
            maps[array[i]] = i
    return False
    


assert not check_sums([], 17)
assert check_sums([10, 15, 3, 7], 17)
assert not check_sums([10, 15, 3, 4], 17)
