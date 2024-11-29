class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s) - 1):
            x = ord(s[i]) - ord(s[i+1])
            sum += abs(x)
        return sum