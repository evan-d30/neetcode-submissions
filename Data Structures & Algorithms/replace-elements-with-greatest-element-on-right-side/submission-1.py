class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i,n in enumerate(arr):
            if i == len(arr)-1:
                arr[i] = -1
                continue
            arr[i] = max(arr[i+1:])
        return arr
