# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        
        while lo < hi:
            m = (lo+hi) // 2
            t = isBadVersion(m)
            if t:
                hi = m
            else:
                lo = m + 1
        return hi