
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = new_node = ListNode(0)
        while l1 or l2 or carry!=0:
            v1 = v2 =0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry , newVal = divmod(v1 + v2 + carry , 10)                   
            new_node.next = ListNode(newVal)    
            new_node = new_node.next
        return root.next