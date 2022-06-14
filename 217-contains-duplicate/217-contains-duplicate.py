class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = sorted(set(nums))
        nums.sort()
        if(list(set_num)==nums):
            return False
        else:
            return True