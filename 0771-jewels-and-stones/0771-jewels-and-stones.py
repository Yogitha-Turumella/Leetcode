class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in stones:
            for j in jewels:
                if j == i:
                    ans+=1
                    break
        return ans