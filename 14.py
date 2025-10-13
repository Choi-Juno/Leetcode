class Solution:
    def LongestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
