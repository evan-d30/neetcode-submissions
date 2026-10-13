class Solution:
    def reverseString(self, s: List[str]) -> None:
        string = "".join(s)
        s[:] = list(string[::-1])
        return s