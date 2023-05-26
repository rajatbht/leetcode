class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a=[2,6,3,4,5,6]
head = llist=ListNode(1)
for item in a:
    llist.next=ListNode(item)
    llist=llist.next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root=result=ListNode()
        while head:
            while head and head.val==val:
                head=head.next
                if head==None:
                    return root.next
            result.next=ListNode(head.val)
            result=result.next
            head=head.next
        return root.next

val=6
b=Solution()
b.removeElements(head,val)