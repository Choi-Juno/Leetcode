# 42. Trapping Rain Water


def trap(height: list[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    volume = 0

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        # 더 높은 쪽을 향해 투 포인터 이동
        # 높은 쪽의 포인터는 현재 위치를 그대로 두고 낮은 쪽의 포인터를 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
