class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        result = False
        
        if(len(s)!=len(t)):
            return False
        
        char_s = [0]*26
        char_t = [0]*26
        
        for i in s:
            char_s[ord(i)-ord("a")]+=1
            
        for i in t:
            char_t[ord(i)-ord("a")]+=1
            
        for i in range(0,26):
            if(char_s[i] == char_t[i]):
                result = True
                
            else:
                return False
            
        return result
            
            