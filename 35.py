# 35. Search Insert Position
def searchInsert(nums: list[int], target: int) -> int:
    nums.append(target)
    nums.sort()
    return nums.index(target)
