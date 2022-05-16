"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

#sample solution
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll= ListNode(-99)
        curr = ll
                
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:   
                curr.next = l2
                curr = l2
                l2 = l2.next
        
        if l2 is None and l1 is not None: curr.next = l1
        if l1 is None and l2 is not None: curr.next = l2
        
        return ll.next
        