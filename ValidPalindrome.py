from collections import deque


def isPalindrome(str: str) -> bool:
    strs = []
    str = str.lower()
    strs = [char for char in str if char.isalnum()]
    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False
    return True


def isPalindrome2(str: str) -> bool:
    # 자료형 Deque 선언
    strs: deque = deque()

    for char in str:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome2("A man, a plan, a canal: Panama"))
