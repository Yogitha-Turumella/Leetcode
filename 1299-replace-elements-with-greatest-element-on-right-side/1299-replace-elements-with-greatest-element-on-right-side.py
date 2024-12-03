class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = max_
            max_ = max(current,max_)
        return arr
        