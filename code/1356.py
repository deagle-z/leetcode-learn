class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for j in range(len(nums)) if i > nums[j]) for i in nums]