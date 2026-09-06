class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapp = {')':'(',']':'[','}':'{'}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1]!=mapp[char]:
                    return False
                stack.pop()
        return True if not stack else False


        '''
        for char in s:
            if char in mapp:
                
                if stack and stack[-1] == mapp[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
        '''