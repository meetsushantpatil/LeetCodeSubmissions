# REACTO - https://www.youtube.com/watch?v=DIR_rxusO8Q&t=87s 
# Repeat - Given 2 sorted lists, merge & create a sorted list as the output.
# Clarifying questions - 1. Can list be empty? 2. Assuming list is not circular. 3. Single or doubly linked lists?
# Examples - 1. list1 = [1,2,3], list = [5,6,7] -> result = [1,2,3,4,5,6] 2. [] + [] -> []
# Approach -   1. O(n) - compare elements & insert
# Code
# Test
# Optimisation


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
                
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
                
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next