from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for ix in range(len(nums)):
            if nums[ix] < target:
                continue
            elif nums[ix] >= target:
                return ix
        return len(nums)

nums = [1,3,5,6]
target = 2
obj = Solution()
print(obj.searchInsert(nums, target))
