class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        pile = []
        cor = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in cor:
                if not pile or cor[c] != pile.pop():
                    return False
            else:
                pile.append(c)
        return not pile