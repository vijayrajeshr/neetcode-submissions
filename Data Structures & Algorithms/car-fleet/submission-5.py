class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = zip(position,speed)
        cars = sorted(list(zipped))
        stack = []
        
        for pos,speed in reversed(cars):
            time = (target-pos)/speed

            if not stack or time>stack[-1]:
                stack.append(time)
        res = len(stack)
        return res