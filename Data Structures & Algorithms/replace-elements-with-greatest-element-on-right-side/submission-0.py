class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        templist = []
        for i,n in enumerate(arr):
            right = arr[i+1:]
            if i == len(arr)-1:
                templist.append(-1)
                continue
            max_num = max(right)
            templist.append(max_num)
        return templist
