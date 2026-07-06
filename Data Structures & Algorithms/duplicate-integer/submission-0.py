class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_1 = set()
        for i in nums:
            if i in hash_1:
                return True
            hash_1.add(i);
    
        return False
