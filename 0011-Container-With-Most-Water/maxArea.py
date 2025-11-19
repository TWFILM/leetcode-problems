def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, w*h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))

nums = [1,1]
print(maxArea(nums))
