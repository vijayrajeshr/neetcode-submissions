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
        
        if cleaned_str[::]==cleaned_str[::-1]:
            return True
        return False