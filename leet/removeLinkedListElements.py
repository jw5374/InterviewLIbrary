# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    if head is None:
        return head
    previous = head
    curr = head
    while curr is not None:
        if curr.val == val:
            previous.next = curr.next
        else:
            previous = curr
        curr = previous.next
    if head is not None and head.val == val:
        head = head.next
    return head
