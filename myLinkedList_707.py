class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self, x = None):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        count = 0
        if self.head is None:
            return -1
        cur = self.head
        while cur is not None:
            if(count == index):
                return cur.val
            else:
                count += 1
                cur = cur.next

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            return
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node
        new_node.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        count = 0
        new_node = Node(val)
        if self.head is None and index == 0:
            self.head = new_node
            return
        if self.head is not None and index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        prev = None

        while cur is not None:
            if(count == index):
                prev.next = new_node
                new_node.next = cur

            prev = cur
            cur = cur.next
            count += 1

        if index == count:
            prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            return -1
        if self.head is not None and index == 0:
            temp = self.head.next
            self.head = temp
            return
        count = 0
        cur = self.head
        prev = None
        while cur.next is not None:
            if(index == count):
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
            count += 1

        if index == count:
            prev.next = None
