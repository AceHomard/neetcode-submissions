class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len (s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            res.append(s[j+1:j + 1 +lenght])
            i = j + lenght + 1
        return res