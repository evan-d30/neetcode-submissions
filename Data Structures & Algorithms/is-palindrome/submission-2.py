class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
        combined = "".join(s.split())
        lower = list(combined.lower())

        for i,l in enumerate(lower):
            if l not in alphabet:
                lower[i] = ""

        combinedfinal = "".join(lower)
        if combinedfinal == combinedfinal[::-1]:
            return True
        else:
            return False
