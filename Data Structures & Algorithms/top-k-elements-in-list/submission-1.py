class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for elm in nums:
            if elm in seen:
                seen[elm]+=1
            else:
                seen[elm]=1
        
        res=sorted(seen,key=seen.get)
        rev=list(reversed(res))

        return rev[:k]