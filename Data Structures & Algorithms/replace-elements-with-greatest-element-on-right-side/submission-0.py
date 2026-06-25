class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            mx = max(arr[i+1:])
            arr[i] = mx
        arr[-1] = -1
        return arr