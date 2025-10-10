# 투 포인터를 이용한 스왑
def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)


# 파이썬다운 방식
def reverseString2(s: list[str]) -> None:
    print(s[::-1])


reverseString(["h", "e", "l", "l", "o"])
reverseString2(["h", "e", "l", "l", "o"])
