class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        
        maxarea = 0
        left = 0
        right = len(heights)-1
        
        while left<right:
            length = min(heights[left],heights[right])
            breadth = right-left
            maxarea = max(maxarea,length*breadth)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
