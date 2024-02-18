# REACTO - https://www.youtube.com/watch?v=DIR_rxusO8Q&t=87s 
# Repeat - Given a string, tell me if it is a palindrome.
# Clarifying questions - 1. Will the string contain non-alphanumeric letters? 2. Case-sensitive?
# Examples - 1. "race a car" -> True, 2. "tst" -> True 3. "#abcba" -> True 4. ""  -> True 5. " " -> True
# Approach -   
# Keep 2 pointers, left & right. If it finds non-alphanumeric, go ahead for left or right. If matches, go ahead, else break && return False. -> O(n)
# Code
# Test
# Optimisation

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) < 2:  
            return True
        
        left_ptr = 0 
        right_ptr = len(s)-1 

        while left_ptr < right_ptr:  

            if s[left_ptr].isalnum() and s[right_ptr].isalnum():
                if s[left_ptr].lower() != s[right_ptr].lower():
                    return False
                else:
                    left_ptr+= 1
                    right_ptr-= 1 
            
            if not s[left_ptr].isalnum():
                left_ptr+= 1
            
            if not s[right_ptr].isalnum():
                right_ptr-= 1

        return True
