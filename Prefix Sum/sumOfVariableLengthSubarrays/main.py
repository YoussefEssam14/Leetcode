class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix_sums = list(itertools.accumulate(nums))
        total = 0
        n = len(nums)
        for i in range(n):
            start = max(0,i-nums[i])
            if start > 0:
                total += prefix_sums[i] - prefix_sums[start-1]
            else:
                total += prefix_sums[i]
        return total