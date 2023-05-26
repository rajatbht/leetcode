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
        root = result = ListNode()
        if head and head.next == None:
            result.next = ListNode(head.val)
            return root.next
        prev = head.val
        head=head.next
        if head.next == None:
                if head.val != prev:
                    result.next = ListNode(prev)
                    result=result.next
                    result.next = ListNode(head.val)
                    return root.next
                return root.next
        while head and head.next:
            if head.val == prev or head.val ==head.next.val:
                prev=head.val
                head = head.next
                if head.next == None:
                    if head.val != prev:
                        result.next = ListNode(head.val)
                        result=result.next
                        return root.next
            else:
                result.next = ListNode(head.val)
                result=result.next
                result.next = ListNode(head.next.val)
                head = head.next
        return root.next

a=[2,3,3,4,4,5]
head = llist=ListNode(1)
for item in a:
    llist.next=ListNode(item)
    llist=llist.next

b=Solution()
b.deleteDuplicates(head)
            
                