class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            if(i in num_dict):
                return True
            else:
                num_dict[i] = "#"
                
        return False