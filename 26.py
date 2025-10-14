# 26. Remove Duplicates from Sorted Array


def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    nums[:] = sorted(set(nums))

    return len(nums)
