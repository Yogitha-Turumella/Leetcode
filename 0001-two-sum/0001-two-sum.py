class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            next = target - num
            if next in nums_dict:
                return [nums_dict[next], i]
            else:
                nums_dict[num] = i
        return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
