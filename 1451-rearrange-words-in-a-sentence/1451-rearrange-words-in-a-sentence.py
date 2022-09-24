class Solution:
    def arrangeWords(self, text: str) -> str:
        a=text.split()
        a[0]=chr(ord(a[0][0])+32)+a[0][1:]
        def key(val):
            return len(val)
        a.sort(key=key)
        a[0]=chr(ord(a[0][0])-32)+a[0][1:]
        return " ".join(a)
    
        