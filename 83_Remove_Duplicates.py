class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root= result =ListNode()
        if head:
            if head.val==0:
                result.next=ListNode()
                result=result.next
        while head:
            v1=head.val
            v2=result.val
            if v1 != v2:
                result.next=ListNode(v1)
                head=head.next
                result=result.next
            else:
                head=head.next
        return root.next

# def deleteDuplicates(self, head):
#     cur = head
#     while cur:
#         while cur.next and cur.next.val == cur.val:
#             cur.next = cur.next.next     # skip duplicated node
#         cur = cur.next     # not duplicate of current node, move to next node
#     return head
        