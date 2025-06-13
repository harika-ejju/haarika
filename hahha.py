def longestIncreasingSubsequence(nums, k):
  n = len(nums)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
  if nums[i] > nums[j] and nums[i] - nums[j] <= k:
            dp[i] = max(dp[i], dp[j] + 1)

      return max(dp)
