# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = []
        
        while(curr):
            if curr in visited:
                return True
            else:
                visited.append(curr)
            curr = curr.next
            
        return False