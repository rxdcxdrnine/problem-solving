package leetcode;


import java.util.Objects;

class LEETCODE_83 {
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