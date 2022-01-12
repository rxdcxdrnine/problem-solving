/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode p = head;
        List<ListNode> visited = new ArrayList<>();
        
        while (!Objects.isNull(p)) {
            p = p.next;
            
            if (visited.contains(p)) {
                return true;
            } else {
                visited.add(p);
            }
        }
        
        return false;
        
    }
}
