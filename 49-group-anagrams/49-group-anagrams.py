class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        string_dict = {}
        sorted_list = []
                
        for i in strs :
            sorted_list.append(''.join(sorted(i)))
     
        if(len(sorted_list)==2):
            if(sorted_list[0]==sorted_list[1]):
                return [[strs[0],strs[1]]]
            else:
                return [[strs[0]],[strs[1]]]
        
        for i in range(0,len(sorted_list)):
            if sorted_list[i] not in string_dict:
                string_dict[sorted_list[i]] = [strs[i]]
            else:
                string_dict[sorted_list[i]].append(strs[i])
                        
                        
                    
        return list(string_dict.values())