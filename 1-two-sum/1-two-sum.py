class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(0,len(nums)):
            num_dict[nums[i]] = i
        
        for i in range(0,len(nums)):
            second_num = target - nums[i]
            if second_num in num_dict:
                if(i!=num_dict[second_num]):
                    return i,num_dict[second_num]
        
        