# Test () 0

class Solution:
    def isValid(self, s: str) -> bool:
        braces_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for brace in s:
            if brace in braces_dict:
                if(stack):
                    top_element = stack.pop()
                else:
                    top_element = "#"
                    
                if(top_element!=braces_dict[brace]):
                    return False
                
            else:
                stack.append(brace)
                
        
        return not stack
            
        
        
        