class Solution:
    def trap(self, height: List[int]) -> int:
        
        rainbox = 0
        leftmax = 0 
        rightmax = 0

        left = 0
        right = len(height)-1

        while left<right:
            if height[left]<height[right]:
                if height[left]>leftmax:
                    leftmax = height[left]
                else:
                    rainbox+=leftmax - height[left]
                    left+=1

            else:
                if height[right]>rightmax:
                    rightmax = height[right]
                else:
                    rainbox+=rightmax - height[right]
                    right-=1
        return rainbox
