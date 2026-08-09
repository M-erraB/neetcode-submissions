class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        maxOnes = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
                maxOnes = max(maxOnes, ones)

            else:
                ones = 0
        return maxOnes
            