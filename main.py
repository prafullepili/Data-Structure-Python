def get_second_largest(nums):
    l = nums[0]
    s_l = None
    for i in range(len(nums)):
        if nums[i] > l:
            l = nums[i]
            s_l = nums[i - 1]
        else:
            if nums[i] < l and nums[i] > s_l:
                s_l = nums[i]
    return s_l, l


def check_sorted(nums):
    for i in range(1, len(nums)):
        if not nums[i] >= nums[i - 1]:
            return False
    return True


def remove_duplicates_in_place(nums):
    i = 1
    while i < len(nums):
        for j in range(i, len(nums)):
            if nums[i - 1] < nums[j] and nums[i - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return nums[:i]


def left_rotate(nums, by=1):
    n = len(nums)
    if by < 1:
        return nums

    d = by % n
    if d == 0:
        return nums
    f = nums[:d]
    i = d
    while i < n:
        nums[i - d] = nums[i]
        i += 1
    for j in f:
        nums[i - d] = j
        i += 1
    return nums


def right_rotate(nums, k=1):
    n = len(nums)
    d = k % n
    right = nums[: n - d]
    j = 0
    for l in nums[n - d :]:
        nums[j] = l
        j += 1
    for r in right:
        nums[j] = r
        j += 1


def Move0toEnd(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.insert(len(nums), 0)
    return nums


def subarray(nums, D):
    longest_sub_arr = []
    l = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s == D:
                sub_arr = []
                for k in range(i, j + 1):
                    sub_arr.append(nums[k])
                if l < max(l, j - i + 1):
                    longest_sub_arr = sub_arr
                l = max(l, j - i + 1)
    return longest_sub_arr, l


def alternatingSubarray(nums):
    n = len(nums)
    res = dp = -1
    for i in range(1, n):
        if dp >= 2 and nums[i] == nums[i - 2]:
            dp += 1
        else:
            if nums[i] == nums[i - 1] + 1:
                dp = 2
            else:
                dp = -1
        res = max(res, dp)
    return res


def subarrayBetter(nums, D):
    # if array have Zeros and positives and nagatives
    s = l = 0
    d = {}
    for i in range(len(nums)):
        s += nums[i]
        if s not in d:
            d[s] = i
        if s == D:
            l = max(l, i + 1)
        elif (s - D) in d:
            l = max(l, i - d[s - D])
    return l


def subarrayOptimal(nums, D):
    # if array have Zeros and positives
    left = right = 0
    s = nums[0]
    m = 0
    n = len(nums)

    while right < n:
        while left <= right and s > D:
            s -= nums[left]
            left += 1
        if s == D:
            m = max(m, right - left + 1)

        right += 1
        if right < n:
            s += nums[right]
    return m


# print(get_second_largest([-11, 20, 4, 7, 9, 8, 5]))
# print(check_sorted([1, 2, 4, 5, 7, 8, 7, 9]))
# print(remove_duplicates_in_place([1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 10]))
# print(right_rotate([1, 2, 3, 4, 5, 6, 7], 3))
# print(Move0toEnd([0, 1, 0, 3, 12]))
# print(subarray([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 17))
# print(subarrayBetter([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 17))
print(subarrayOptimal([1, 2, 3, 1, 1, 1, 1, 3, 3], 6))
# print(alternatingSubarray([2,3,4,3,4]))
