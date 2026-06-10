class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''

        for ch in s:
            if (ord(ch) >=97 and ord(ch) <= 122) or \
            (ord(ch) >= 65 and ord(ch) <= 90) or \
            (ord(ch) >= 48 and ord(ch) <= 57):
                stripped += ch.lower()

        # print(stripped)

        p1, p2 = 0, len(stripped)-1

        while p2 > p1:
            if stripped[p1] == stripped[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True