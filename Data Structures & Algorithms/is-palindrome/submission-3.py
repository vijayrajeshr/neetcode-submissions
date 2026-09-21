class Solution(object):          # valid palindrome
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        """
        cleaned_str = ""
        for char in range(len(s)):
            if s[char].isalnum():
                lowered_char = s[char].lower()
                cleaned_str+=lowered_char
        '''
        if cleaned_str[::]==cleaned_str[::-1]:
            return True
        return False
        '''
        '''
        Two Pointer Approach -->
        '''
        left = 0
        right = len(cleaned_str)-1

        while left<right:
            if cleaned_str[left]!=cleaned_str[right]:
                return False
            left+=1
            right-=1
            

        return True




