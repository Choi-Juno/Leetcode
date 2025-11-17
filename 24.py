# 24. Swap Nodes in Pairs
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 값만 교환
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        current.val, current.next.val = current.next.val, current.val
        current = current.next.next

    return head


# 반복 구조로 스왑
def swapPairs2(head: Optional[ListNode]) -> Optional[ListNode]:
    root = prev = ListNode(0)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next


# 재귀 구조로 스왑
def swapPairs3(head: Optional[ListNode]) -> Optional[ListNode]:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = swapPairs3(p.next)
        p.next = head
        return p
    return head
