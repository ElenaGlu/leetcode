from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for obj in nums:
            ix = nums.index(obj)
            obj_one = obj
            for el in nums[ix + 1:]:
                obj_two = el
                if obj_one + obj_two == target:
                    return [nums.index(obj_one), nums.index(obj_two)]


nums = [3, 3]
target = 6
obj = Solution()
print(obj.twoSum(nums, target))
