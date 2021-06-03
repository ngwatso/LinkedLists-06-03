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

