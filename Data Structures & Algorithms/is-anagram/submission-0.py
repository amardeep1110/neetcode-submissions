class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new1 = "".join(sorted(s))
        new2 = "".join(sorted(t))
        if new1 == new2:
            return True
        else:
            return False