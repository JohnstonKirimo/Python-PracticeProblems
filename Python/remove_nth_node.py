"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
#solution

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        n_inorder = length - n + 1
        pre, cur = None, head
        index = 1 
        while cur:
            if index == n_inorder:
                if pre is None:
                    head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                index += 1
                pre = cur
                cur = cur.next
        return head
