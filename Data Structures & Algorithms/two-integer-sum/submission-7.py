class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashm:
                return [hashm[diff],i]
            hashm[num]=i