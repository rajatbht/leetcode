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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head.next==None:
            return head
        
        curr=self.reorderList(head.next)
        head.next=curr

        while curr.next:
            curr=curr.next
            
        curr.next=head
        root=head=curr
        while curr.next!=head:
            curr=curr.next
        curr.next=None
        return root

b=Solution()
b.reorderList(head)
# 4, 5   -> 5,4       #1,5,2,4,3
# 3, 5,4 -> 4,3,5
# 2, 4,3,5 -> 5,2,3,4  || 5,2,4,3
# 1, 5,2,3,4 -> 1,5,2,4,3
