class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sums = n * (n+1)//2
        sum1 = sum(nums)
        return sums - sum1