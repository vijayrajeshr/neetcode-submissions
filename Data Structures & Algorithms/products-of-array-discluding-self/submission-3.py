class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=[1]*len(nums)
        prefix=1
        for i in range(len(nums)-1):
            prefix=nums[i]*prefix
            n[i+1]=prefix
        sufix=1
        for i in range(len(nums)-1,0,-1):
            sufix=nums[i]*sufix
            sufix1=sufix*n[i-1]
            n[i-1]=sufix1
        return n