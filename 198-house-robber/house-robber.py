# REACTO

# Repeat - Given a list of numbers, pick numbers in a such a way that you get the max sum, but the 2 numbers can not be adjacent
# Approach - Bottom Up Dynamic Programming
# Code - 
# Test - Works
# Optimize - Storage can be optimized

# Test 1
# inputs = [1,2,1,15,6]
# memo =   [1,2,2,17,17]

# Test 2
# inputs = [1,2,3,1]
# memo =   [1,2,4,0]

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0 :
            return 0
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = [0]*len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2])

        return memo[len(nums)-1]

        