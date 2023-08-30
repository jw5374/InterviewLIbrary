class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    linkedNodes = []
    curr = head
    while curr is not None:
        linkedNodes.append(curr)
        curr = curr.next
    return linkedNodes[len(linkedNodes) // 2]
