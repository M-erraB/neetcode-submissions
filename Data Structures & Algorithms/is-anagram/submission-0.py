class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        for char in s:
            if char in counts_s:
                counts_s[char] += 1
            else:
                counts_s[char] = 1
        for char in t:
            if char in counts_t:
                counts_t[char] += 1
            else:
                counts_t[char] = 1
        if counts_t == counts_s:
            return True
        return False