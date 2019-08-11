def get_sliding_max(nums, k):
    windmax = []
    if not nums or not k:
        return windmax
    
    queue = collections.deque()
    
    for i in range(len(nums)):
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
        
        if queue[0] == i - k:
            queue.popleft()
            
        if i >= k - 1:
            windmax.append(nums[queue[0]])
            
    return windmax


assert get_sliding_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert get_sliding_max([5, 2, 1], 2) == [5, 2]
