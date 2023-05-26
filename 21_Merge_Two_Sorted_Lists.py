class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a=[2,4]
b=[3,4]
l1 = llist=ListNode(1)
l2 = llist2=ListNode(1)

for item in a:
    llist.next=ListNode(item)
    llist=llist.next
for item in b:
    llist2.next=ListNode(item)
    llist2=llist2.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final=root=ListNode()
        while l1 or l2:
            v1=v2=None
            if l1:
                v1=l1.val
            if l2:
                v2=l2.val
            if v1==None:
                root.next=ListNode(v2)
                root=root.next
                l2=l2.next
            elif v2==None or v1<v2:
                root.next=ListNode(v1)
                root=root.next
                l1=l1.next
            else:
                root.next=ListNode(v2)
                root=root.next
                l2=l2.next                            
        return final.next

c=Solution()
c.mergeTwoLists(l1,l2)