class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        k = 0
        ans = []
    
        while k < 2:
            ans.append(nums[i])
            i += 1

            if i == len(nums):
                i = 0
                k += 1
        return ans

        



        
