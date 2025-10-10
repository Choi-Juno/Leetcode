from collections import deque
import re


# 리스트로 변환
def isPalindrome(str: str) -> bool:
    strs = []
    str = str.lower()
    strs = [char for char in str if char.isalnum()]
    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False
    return True


# 데크 자료형을 이용한 최적화
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


# 슬라이싱 사용
def isPalindrome3(str: str) -> bool:
    str = str.lower()
    str = re.sub("[^a-z0-9]", "", str)
    return str == str[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome3("A man, a plan, a canal: Panama"))
