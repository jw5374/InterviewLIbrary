# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    # strNum = ""
    # currNode = head
    # while currNode is not None:
    #     strNum += str(currNode.val)
    #     currNode = currNode.next
    # return int(strNum, 2)
    digits = []
    currNode = head
    while currNode is not None:
        digits.append(currNode.val)
        currNode = currNode.next
    res = 0
    length = len(digits) - 1
    for i in range(length, -1, -1):
        res += digits[i] * (2 ** (length - i))
    return res
