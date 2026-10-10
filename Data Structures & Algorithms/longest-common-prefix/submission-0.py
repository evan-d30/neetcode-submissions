class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newlist = list(zip(*strs))
        string = ""
        for s in newlist:
            if len(set(s)) ==1:
                string += s[0]
            else:
                break
        return string