class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        while lo <= hi:
            m = math.floor(lo + (hi - lo) / 2)
            m_raiz = m * m
            
            if m_raiz == x:
                return abs(m)
            elif m_raiz < x: 
                lo = m + 1
            else:
                hi = m - 1
        return abs(hi)