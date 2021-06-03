# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    
    if l1 is None:
        return l2
    if l2 is None:
        return l1
        
    if (l1.value < l2.value):
        l1.next = mergeTwoLinkedLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLinkedLists(l2.next, l1)
        return l2

# ===============

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def printList(l):
    LL = l
    while LL:
        print(LL.value, end="--> ")
        LL = LL.next
    print("None")
    
def insertValueIntoSortedLinkedList(l, value):
    
    curr = l
    newNode = ListNode(value)
    print('newNode', newNode.value)
    
    if (curr == None):
            l = newNode
            return l
    
    while curr != None:
        if (curr.value > newNode.value):
            newNode.next = l
            l = newNode
            printList(l)
            return l
        elif (curr.next == None):
            curr.next = newNode
            printList(l)
            return l
        elif (curr.next.value > newNode.value):
            printList(l)
            newNode.next = curr.next
            printList(l)
            curr.next = newNode
            printList(l)
            
            curr = curr.next
            printList(l)
            return l
        else:
            curr = curr.next
    
        
        
    return l

# ===============

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        binStr = ""        
        curr = head
        
        while curr is not None:
            binStr += str(curr.val)
            curr = curr.next
            
        return int(binStr, 2)

# ===============

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        currSlow = head
        currFast = head
        
        while currFast and currFast.next:
            currSlow = currSlow.next
            currFast = currFast.next.next
            
        return currSlow

# ===============