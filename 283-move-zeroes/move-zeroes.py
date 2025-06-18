"""
Repeat - I need reorder array elements, all zeroes to the end. 
Examples - [1, 0, 15] -> [1, 15, 0], [0] -> [0]
Approach - Delete element in array, Doubly linked list (easy remove and insert), Queue (read all elements one by one, count # of 0s)
Code
Test
Optimize 

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[non_zero] = nums[i]
                non_zero += 1 

        for j in range(non_zero, len(nums)):
            nums[j] = 0
            

        

