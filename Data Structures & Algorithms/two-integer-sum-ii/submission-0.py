class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        print(left, right)
        while left < right:
            somme = numbers[left] + numbers[right]
            if somme > target:
                right -= 1
            elif somme < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []