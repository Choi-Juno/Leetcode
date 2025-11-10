# 206. Reverse Linked List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# 재귀 구로 뒤집기
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# 반복 구조로 뒤집기
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
