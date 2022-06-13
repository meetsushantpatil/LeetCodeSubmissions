class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        min_len = float('inf')
        
        for word in strs:
            if(len(word)<min_len):
                min_len = len(word)
        
        for i in range(min_len):
            temp_char = ""
            matches = 0
            for j in range(len(strs)):
                if((temp_char)==""):
                    temp_char=strs[j][i]
                    matches+=1
                    continue
                elif(temp_char==strs[j][i]):
                    matches+=1
                    continue
                else:
                    return longest_prefix
            if(matches==len(strs)):        
                longest_prefix+=temp_char
            
        return longest_prefix
                    
            
            
            
                