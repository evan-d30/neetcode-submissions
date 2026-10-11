class Solution:
    def calPoints(self, operations: List[str]) -> int:
        templist = []
        for index,s in enumerate(operations):
            if s == "+":
                templist.append(templist[-1]+templist[-2])
            elif s == "C":
                templist.remove(templist[-1])
            elif s == "D":
                templist.append(templist[-1]*2)
            else:
                templist.append(int(s))

        return sum(templist)