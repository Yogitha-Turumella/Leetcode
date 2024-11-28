from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_c = Counter(s)
        for index,char in enumerate(s):
            if char_c[char] == 1:
                return index
        return -1
        