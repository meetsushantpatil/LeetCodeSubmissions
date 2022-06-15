class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        
        
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        
        for i in nums[1:]:
            
            temp_max = max(i,max_product*i,min_product*i)
            min_product = min(i,max_product*i,min_product*i)
            
            max_product = temp_max
            
            result = max(max_product,result)
            
        return result
            
            