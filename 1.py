# 1. Two Sum
class Solution:
    # 1. Brute Force를 이용한 방법
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 2. in을 이용한 방법
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i + 1 :]:
                return [i, nums[i + 1 :].index(complement) + i + 1]
        return []

    # 3. 첫 번째 수를 뺸 결과 키 조회
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 키와 값을 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
        return []

    # 4. 조회 구조 개선
    def twoSum4(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
        return []
