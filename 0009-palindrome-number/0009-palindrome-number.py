class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        
        if len(string) == 2:
            return string[0] == string[1]
                
        
        if string == string[::-1]:
            return True
        else:
            return False
        
#         array = list(string)
        
#         array = array[1:-1]
        
#         arr = [int(c) for c in array]
        
#         res_xor = 0
        
#         for num in arr:
#             res_xor ^= num
        
#         return res_xor == 0