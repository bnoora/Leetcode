class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)-1
        m = 0
        if len(s) == 0:
            return True

        while m < n:
            while m < n and not (s[m].isalnum()):
                m += 1
            while m < n and not (s[n].isalnum()):
                n -= 1
            if s[m].lower() != s[n].lower():
                return False
            m += 1
            n -= 1
        return True


    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )