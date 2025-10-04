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

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7])) # output: 49
    print(maxArea([1,1]))               # output: 1
    print(maxArea([4,3,2,1,4]))         # output: 16
    print(maxArea([1,2,1]))             # output: 2