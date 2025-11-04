# 234. Palindrome Linked List
from collections import deque
from typing import Deque, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 리스트 변환
def isPalindrome1(head: Optional[ListNode]) -> bool:
    q: list = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True


# 2. 데크를 이용한 최적화
def isPalindrome2(head: Optional[ListNode]) -> bool:
    q: Deque = deque()

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


# 3. 런너를 이용한 풀이
def isPalindrome3(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast and slow:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and slow and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
