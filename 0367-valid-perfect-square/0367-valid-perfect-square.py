class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 0, num

        while lo <= hi:
            m = (lo + hi) // 2
            target = m * m
            if target == num:
                if isinstance(target, int):
                    return True
                else:
                    return False
            elif target > num:
                hi = m - 1
            else:
                lo = m + 1