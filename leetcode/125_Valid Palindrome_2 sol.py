# sol1
class Solution(object):
    def isPalindrome(self, s):
        l = []
        for c in s:
            if (c.isalpha() or c.isnumeric()): # if c.alnum():
                l.append(lower(c))
        if l[::-1] == l: # return l[::-1] == l
            return True
        else: return False

# sol2
class Solution2(object):
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

# what I learned
# 1. str.alnum()
# 2. [c.lower() for c in s if c.isalnum()] 로 한 줄로 표현하는 방법
# 3. all (iterable) -> if all True: True; else: False
# 4. any (iterable) -> if any True: True; else: False
# 5. ~i = -i-1
