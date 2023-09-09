# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    i = 0
    num1 = 0
    num2 = 0
    l1node = l1
    l2node = l2
    while l1node is not None:
        num1 += l1node.val * (10 ** i)
        i += 1
        l1node = l1node.next
    i = 0
    while l2node is not None:
        num2 += l2node.val * (10 ** i)
        i += 1
        l2node = l2node.next
    resNum = num1 + num2
    res = ListNode()
    currNode = res
    while resNum > 0:
        currNode.val = resNum % 10
        currNode.next = ListNode()
        if resNum // 10 == 0:
            currNode.next = None
        resNum //= 10
        currNode = currNode.next
    return res
