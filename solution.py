class Solution(object):
    def isPalindrome(self, s):
        result = ""
        for i in range(len(s)):  
            if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9': 
                result += s[i]
            elif 'A' <= s[i] <= 'Z':  
                result += chr(ord(s[i]) + 32)  
            else:
                continue

        s=result
        print(result)

        i=0
        j=len(s)-1
        while i<=j:
            if s[i]==' ':
                i+=1
                continue
            elif s[j]==' ':
                j-=1
                continue
            elif s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        