def maximumSubarraySum(nums:list, k: int) -> int:
    res = 0
    prev_idx = {}
    cur_sum = 0

    left = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
    
        i = prev_idx.get(nums[right],-1)

        while left <= i or right - left + 1 > k:
            cur_sum -= nums[left]
            left += 1
        
        if right - left + 1 == k:
            res = max(res, cur_sum)
        
        prev_idx[nums[right]] = right
    
    return res

nums = [1,5,4,2,9,9,9]
k = 3
maximumSubarraySum(nums,k)