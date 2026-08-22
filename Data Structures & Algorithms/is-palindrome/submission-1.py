class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean(s):
            result=""
            for char in s:
              if char.isalnum():  
                result+=char.lower()
            return result
        s=clean(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False 
            i+=1
            j-=1
        return True 