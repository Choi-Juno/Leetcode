# 136. Single Number
def singleNumber(nums: list[int]) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num
    return 0
