def deduplication(nums):
    visited = set()
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] in visited:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        else:
            visited.add(nums[start])
            start += 1
    return start

def deduplication2(nums):
    d, result = {}, 0
    for num in nums:
        if num not in d:
            d[num] = True
            nums[result] = num
            result += 1

    return result

nums = [1,3,1,4,4,2]
# nums = [1]
print deduplication2(nums)