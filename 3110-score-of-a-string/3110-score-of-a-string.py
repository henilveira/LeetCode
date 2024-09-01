class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = list(s)
        
        score = 0
        for i in range(len(arr)-1):
            
            score += abs(ord(arr[i]) - ord(arr[i + 1]))
        return score