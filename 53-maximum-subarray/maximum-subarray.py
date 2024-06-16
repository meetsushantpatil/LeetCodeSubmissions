class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = 0

        for i in nums :
            if current_sum < 0 :
                current_sum = i
            
            else:
                current_sum += i

            max_sum = max(current_sum, max_sum)

        return max_sum
        