class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def get(self, index):
        if self.size<=index or index<0:
            return -1
        if self.head==None:
            return -1
        last=self.head
        for i in range(index):
            last=last.next
        return last.data
    # ADD AT LAST
    def addAtTail(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            print(self.head.data)
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node
        self.size+=1
        print(last.next.data)
    # ADD AT THE BEGINING
    def addAtHead(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1
        print(self.head.data)
    # ADD AT INDEX
    def addAtIndex(self, index, data):
        new_node=Node(data)
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(self,data)
        else:
            last=self.head
            for i in range(index-1):
                last=last.next
            next_node=last.next
            last.next=new_node
            new_node.next=next_node
            self.size+=1

        # counter=1
        # last=self.head
        # while counter!=index:
        #     last=last.next
        #     counter+=1
        # if last==None:
        #     return
        # new_node.next=last.next
        # last.next=new_node

    # DELETE AT INDEX
    def deleteAtIndex(self, index):
        if index<0 or index>=self.size:
            return 
        if self.head==None:
            return
        last=self.head
        if index==0:
            self.head=last.next
        else:
            for i in range(index-1):
                last=last.next
            last.next=last.next.next
        self.size-=1
        
    # ADD DATA AFTER GIVEN ELEMENT
    # def add_after(self,data,after):
    #     new_node=Node(data)
    #     if self.head==None:
    #         return "list deosnt exist"
    #     desired_location=self.head
    #     while desired_location.data!=after:
    #         desired_location=desired_location.next
    #     new_node.next=desired_location.next
    #     desired_location.next=new_node
    #     print(desired_location.data)
    #     print(desired_location.next.data)

    # DELETE
    # def delete(self,data):
    #     if self.head==None:
    #         return "no elements to delete"
    #     if self.head.data==data:
    #         self.head=None
    #         return
    #     del_element=self.head
    #     while del_element.next.data!=data:
    #         del_element=del_element.next
        
    def printList(self):
        new_node=Node()
        if self.head==None:
            return "no elements to show"
        while self.head:
            print(str(self.head.data)+"-->" ,end="")
            self.head=self.head.next
        print("")
            
a=LinkedList()
a.get(0)
a.deleteAtIndex(0)

a.addAtTail(2)
a.addAtTail(3)

a.deleteAtIndex(0)
a.printList()
a.addAtTail(4)
a.addAtTail(6)
a.get(0)
a.get(3)
# a.addAtHead(9)
# a.addAtHead(8)
# a.addAtHead(7)
# a.addAtHead(3)

a.addAtIndex(0,1)
a.addAtIndex(0,0)
a.addAtIndex(5,5)
a.addAtIndex(7,7)
a.addAtIndex(8,8)
a.addAtIndex(9,9)
a.addAtIndex(10,10)
a.get(0)
a.get(10)
a.get(20)
# a.add_after(4,3)
# a.add_after(5,4)
# a.add_after(6,5)
# a.printList()
a.deleteAtIndex(4)
a.deleteAtIndex(1)
a.printList()
