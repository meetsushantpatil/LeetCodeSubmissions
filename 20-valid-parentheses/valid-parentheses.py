# REACTO - https://www.youtube.com/watch?v=DIR_rxusO8Q&t=87s 
# Repeat - Get a string with 3 types of braces, determine if it is valid. Sequence matters, type matters.
# Clarifying questions -> Will there be any characters other than braces ever? Empty string? 
# Examples -> "[{()}]" -> Valid, "{[}]" -> invalid, ")()" -> invalid, ")(" -> invalid, "[)]" -> invalid
# Approach -> Possible approaches 1. Stack O(n) 
# Code
# Test
# Optimisation

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracesDict = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for char in s:
            
            if char in bracesDict:
                top_element = stack.pop() if stack else "#"

                if(top_element != bracesDict[char]):
                    return False
            else:
                stack.append(char)
        
        return not stack

        

                




        
        