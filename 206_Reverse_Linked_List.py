class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a=[2,3,4,5]
head = llist=ListNode(1)
for item in a:
    llist.next=ListNode(item)
    llist=llist.next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return
        if head.next==None:
            return head
        curr=self.reverseList(head.next)
        prev=head
        curr.next=prev
        while head!=curr:
            head=head.next
        head.next=None
        return curr

b=Solution()
b.reverseList(head)
        
        