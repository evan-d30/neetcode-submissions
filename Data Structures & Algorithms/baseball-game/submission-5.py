class Solution:
    def calPoints(self, operations: List[str]) -> int:
        templist = []
        for s in operations:
            if s == "+":
                templist.append(templist[-1]+templist[-2])
            elif s == "C":
                templist.pop()
            elif s == "D":
                templist.append(templist[-1]*2)
            else:
                templist.append(int(s))
        return sum(templist)