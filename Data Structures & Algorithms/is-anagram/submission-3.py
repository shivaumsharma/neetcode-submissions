class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = collections.Counter(s)
        for char in t:
            if seen[char] <= 0:
                return False 
            seen[char] -= 1
        return True