class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols=len(encodedText)//rows
        ans=[]
        i=0
        j=0
        while(j<cols): 
            if(i==rows-1):
                node=(i*cols)+j
                ans.append(encodedText[node])
                curr=j-i+1
                i=0
                j=curr
            else:
                node=(i*cols)+j
                ans.append(encodedText[node])
                i+=1
                j+=1
        j=len(ans)-1
        while(j>=0 and ans[j]==" "):
            j-=1
        return "".join(ans[:j+1])
        
            