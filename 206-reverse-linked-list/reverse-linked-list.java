/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode newList = null;
        ListNode current = head;
        ListNode nextNode = null;

        System.out.println(current);

        while(current != null){
            nextNode = current.next;
            current.next = newList;
            newList = current;
            current = nextNode;
        }
        return newList;
    }
    
}