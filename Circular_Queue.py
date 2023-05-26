class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class MyCircularQueue(object):
    def __init__(self,k):
        self.head=None
        self.tail=None
        self.max_size=k
        self.size=0
    def enQueue(self, value):
        if self.isFull():
            return False
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.head.prev=self.tail
            self.size+=1
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.head.prev=self.tail
            self.size+=1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.size==1:
            self.head=self.head.next
            self.tail=self.head
            self.size-=1
            return True
        else:
            self.head=self.head.next
            self.head.prev=self.tail
            self.size-=1
            return True      

    def Front(self):
        if self.size==0:
            return -1
        return self.head.data
        

    def Rear(self):
        if self.size==0:
            return -1
        return self.tail.data
        

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def isFull(self):
        if self.size==self.max_size:
            return True
        return False

myCircularQueue = MyCircularQueue(81)
myCircularQueue.enQueue(69)
myCircularQueue.deQueue()
myCircularQueue.enQueue(92)
myCircularQueue.enQueue(12)
myCircularQueue.deQueue()
myCircularQueue.isFull() 
myCircularQueue.isFull() 
myCircularQueue.Front()
myCircularQueue.deQueue()
myCircularQueue.enQueue(28)
myCircularQueue.Front()
