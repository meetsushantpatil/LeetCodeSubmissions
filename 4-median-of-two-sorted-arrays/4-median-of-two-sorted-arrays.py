# nums1 = [1,2], nums2 = [0,4]

class Solution:
    def findMedianSortedArrays(self,nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(nums1+nums2)

        if(len(merged_array)%2==0):
            return (merged_array[int(len(merged_array)/2)-1] + merged_array[int(len(merged_array)/2)])/2

        else:
            return merged_array[int(len(merged_array)/2)]