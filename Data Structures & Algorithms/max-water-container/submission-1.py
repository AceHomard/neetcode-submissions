class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0
        while left < right:
            hl = heights[left]
            hr = heights[right]
            if hl > hr:
                tmp = hr * (right - left)
                right -= 1
            else:
                tmp = hl * (right - left)
                left += 1
            if tmp > best:
                    best = tmp
        return best