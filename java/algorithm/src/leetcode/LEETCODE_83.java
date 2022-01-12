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
    public ListNode deleteDuplicates(ListNode head) {
        
        if (Objects.isNull(head)) {
            return head;
        }
        
        ListNode prev = head;
        ListNode p = prev.next;
        
        while (!Objects.isNull(p)) {
            
            if (prev.val == p.val) {
                prev.next = p.next;
            } else {
                prev = prev.next;                
            }
            
            p = prev.next;
        }
            
        return head;
    }
}