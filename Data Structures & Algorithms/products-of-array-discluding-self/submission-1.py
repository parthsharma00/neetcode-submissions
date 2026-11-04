class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        left = 1
        for i in range(len(nums)):
            output.append(left)      # store BEFORE including nums[i]
            left = left * nums[i]

        right = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] = output[j] * right   # multiply BEFORE including nums[j]
            right = right * nums[j]

        return output