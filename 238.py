# 238. Product of Array Except Self
def productExceptSelf(nums: list[int]) -> list[int]:
    result = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        result.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        result[i] = result[i] * p
        p = p * nums[i]
    return result
