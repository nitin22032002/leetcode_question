class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        ans=0
        arr=self.search(A+A,B)
        if(len(arr)!=0 and arr[0]+len(B)<=len(A)):
            return 1
        elif(len(arr)!=0):
            return 2
        arr=self.search(B,A)
        # print(arr,B)
        if(len(arr)==0):
            return -1
        i=arr[0]
        indexTaken=[i]
        ans+=1
        for item in arr[1:]:
            if(item<i+len(A)):
                continue
            elif(item!=i+len(A)):
                return -1
            i=item
            indexTaken.append(i)
            ans+=1
        j=indexTaken[-1]
        # print(arr,indexTaken,B)
        if(not A.endswith(B[:indexTaken[0]]) or not A.startswith(B[j+len(A):])):
            return -1
        if(arr[0]!=0):
            ans+=1
        if(j+len(A)!=len(B)):
            ans+=1
        return ans
    def search(self,text,pattern):
        i=0
        j=0
        ans=[]
        lps=self.__generateLps(pattern=pattern)
        while(i<len(text)):
            if(j==len(pattern)):
                ans.append(i-j)
                j=lps[j-1]
            elif(text[i]==pattern[j]):
                i+=1
                j+=1
            else:
                if(j!=0):
                    j=lps[j-1]
                else:
                    i+=1
        if(j==len(pattern)):
            ans.append(i-j)
        return ans
    def __generateLps(self,pattern):
        i=1
        j=0
        lps=[0 for _ in range(len(pattern))]
        while(i<len(pattern)):
            if(pattern[i]==pattern[j]):
                j+=1
                lps[i]=j
                i+=1
            else:
                if(j!=0):
                    j=lps[j-1]
                else:
                    lps[i]=0
                    i+=1
        return lps