class Solution(object):          # valid palindrome
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        """
        cleanstr = ""
        for char in s:
            if char.isalnum():
                lowered_char = char.lower()
                cleanstr+=lowered_char
        # two pointer approach
        
        left = 0
        right = len(cleanstr)-1

        while left<right:
            if cleanstr[left]!=cleanstr[right]:
                return False
            else:
                left+=1
                right-=1
        return True