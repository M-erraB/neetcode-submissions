class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.tail is None:
            self.tail = newNode 
            self.head = newNode            
        else:
            self.tail.next = newNode 
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        
        #Check if ListNode is empty
        if self.head is None:
            if index == 0:
                self.head = newNode
                self.tail = newNode
            return
        #Assign a counter to the top of the ListNode
        curr = self.head

        #If the index is 0, simply move the existing head into newNode.next, then replace self.head with newNode
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        #For indices 1 - n-1:
        for i in range(index - 1):
            curr = curr.next if curr else None
        if curr is None:
            return
        newNode.next = curr.next
        curr.next = newNode

        if newNode.next is None:
            self.tail = newNode #If newNode is the last node.

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        curr = self.head
        for i in range(index - 1):
            curr = curr.next if curr else None
        
        if curr is None or curr.next is None:
            return
        curr.next = curr.next.next
        
        if curr.next is None:
            self.tail = curr
        return


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)