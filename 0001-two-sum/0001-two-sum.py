class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            next = target - num
            if next in nums_dict:
                return [nums_dict[next], i]
            else:
                nums_dict[num] = i
        return[]
