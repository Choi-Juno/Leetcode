# 28. Find the Index of the First Occurrence in a String


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
