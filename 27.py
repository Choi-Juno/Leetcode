# 27. Remove Element


def removeElement(nums: list[int], val: int) -> int:
    if not nums:
        return 0

    nums[:] = [num for num in nums if num != val]

    return len(nums)
