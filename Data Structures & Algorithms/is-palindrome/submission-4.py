class Solution(object):          # valid palindrome
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        """
        cln_str = ""
        for char in s:
            if char.isalnum():
                low_char = char.lower()
                cln_str+=low_char
        left = 0
        right = len(cln_str)-1
        
        while left<right:
            if cln_str[left]!=cln_str[right]:
                return False
            else:
                left+=1
                right-=1

        return True
