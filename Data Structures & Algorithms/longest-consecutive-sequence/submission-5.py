class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 0
        numset = set(nums)
        res = 0

        for elm in numset:
            if elm-1 not in numset:
                length=1

                while elm+length in numset:
                    length+=1
            res = max(length,res)
        return res        





