def get_missing_number(nums):
    if not nums:
        return 1
    
    n = len(nums)
    
    for i in range(n):
        while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
            nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
    
    missing = 0
    while missing < n and nums[missing] == missing + 1:
        missing += 1
    
    return missing + 1


assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1
