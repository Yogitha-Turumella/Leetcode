class Solution:
    def hammingWeight(self, n: int) -> int:
        binn = bin(n)
        c=binn.count('1')
        return c