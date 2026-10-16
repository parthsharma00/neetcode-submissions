class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                    if nums[j] + nums[i] == target:
                        return [i,j]
                else:
                    j = j + 1
        