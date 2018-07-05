def findNumberOfLIS(nums):
    dp = [[1, 1] for i in range(len(nums))]
    max_for_all = 1
    for i, num in enumerate(nums):
        max_len, count = 1, 0
        for j in range(i):
            if nums[j] < num:
                if dp[j][0] + 1 > max_len:
                    max_len = dp[j][0] + 1
                    count = 0
                if dp[j][0] == max_len - 1:
                    count += dp[j][1]
        dp[i] = [max_len, max(count, dp[i][1])]
        max_for_all = max(max_len, max_for_all)
    return sum([item[1] for item in dp if item[0] == max_for_all])

def findNumberOfLIS1(nums):
    if nums == []:
        return 0
    length, cnt = [1] * len(nums), [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                if length[i] == length[j] + 1:
                    cnt[i] += cnt[j]
                elif length[i] < length[j] + 1:
                    cnt[i] = cnt[j]
                    length[i] = length[j] + 1
    return sum((y for x, y in zip(length, cnt) if x == max(length)))


nums = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
print findNumberOfLIS1(nums)