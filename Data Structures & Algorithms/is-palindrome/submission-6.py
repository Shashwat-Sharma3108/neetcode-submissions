class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        l = 0
        r = len(s)-1
        
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True
    
    def alphaNum(self, key):
            return (
                ord('A') <= ord(key) <= ord('Z') or
                ord('a') <= ord(key) <= ord('z') or
                ord('0') <= ord(key) <= ord('9')
            )