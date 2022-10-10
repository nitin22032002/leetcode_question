class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if(len(palindrome)==1):
            return ""
        palindrome=list(palindrome)
        n=len(palindrome)
        mid=n//2
        i=0
        while(i<mid):
            if(palindrome[i]!='a'):
                palindrome[i]="a"
                break
            i+=1
        if(i==mid):
            palindrome[-1]="b"
        return "".join(palindrome)