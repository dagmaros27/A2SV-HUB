# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:
            
    class Node:
        
        def __init__(self,val):
            self.val = val
            self.next = None
 
    def __init__(self):
        self.head = self.Node(None)
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head
        i = 0
        
        while i < index:
            curr = curr.next
            i += 1
        
        return  curr.val
        

    def addAtHead(self, val: int) -> None:
        
        if not self.head.val :
            self.head.val = val
        else:
            newNode = self.Node(val)
            newNode.next = self.head
            self.head = newNode
        self.length += 1
       

    def addAtTail(self, val: int) -> None:
        
        if not self.head.val :
            self.head = self.Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            newNode = self.Node(val)
            curr.next = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        newNode = self.Node(val)
        curr = self.head
        i = 0
        while i < index-1:
            curr = curr.next
            i += 1
        newNode.next = curr.next
        curr.next = newNode
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            i = 0
            while i < index - 1:
                curr = curr.next
                i += 1
            curr.next = curr.next.next        
        self.length -= 1
