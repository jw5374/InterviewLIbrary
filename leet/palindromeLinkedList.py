# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:
    stackcheck = []
    currNode = head
    while currNode is not None:
        stackcheck.append(currNode.val)
        currNode = currNode.next
    [i, j] = [0, len(stackcheck)-1]
    while i < j:
        if stackcheck[i] != stackcheck[j]:
            return False
        i += 1
        j -= 1
    return True
