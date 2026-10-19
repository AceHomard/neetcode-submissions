class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        pile = []
        pairs = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in pairs:
                if not pile or pairs[c] != pile.pop():
                    return False
            else:
                pile.append(c)
        return not pile