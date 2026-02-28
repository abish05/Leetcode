class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        length = 0  # current bit length
        
        for i in range(1, n + 1):
            # If i is a power of 2, its binary length increases
            if (i & (i - 1)) == 0:
                length += 1
            
            # Shift result left by current bit length and add i
            result = ((result << length) | i) % MOD
        
        return result