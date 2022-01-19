package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class LEETCODE_141 {
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
