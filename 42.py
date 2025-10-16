# 42. Trapping Rain Water


# 1. Two Pointers를 최대로 이동
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


# 2. Stack을 이용한 풀이
def trap2(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
