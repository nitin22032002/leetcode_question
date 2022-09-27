class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l=list(dominoes)
        i=-1
        j=0
        isPoint=False
        while(j<len(l)):
            while(j<len(l) and l[j]!="."):
                i+=1
                j+=1
            while(j<len(l) and l[j]=="."):
                j+=1
            self.fill(l,i,j)
            i=j
            j+=1
        return "".join(l)
    def fill(self,l,i,j):
        # print(l,i,j)
        if(i==-1 and j==len(l)):
            return
        elif(i==-1):
            if(l[j]=="R"):
                return 
            else:
                j-=1
                while(j>i):
                    l[j]="L"
                    j-=1
        elif(len(l)==j):
            if(l[i]=="L"):
                return
            else:
                i+=1
                while(i<j):
                    l[i]="R"
                    i+=1
        else:
            if(l[i]=="R" and l[j]=="L"):
                i+=1
                j-=1
                while(i<j):
                    l[i]="R"
                    l[j]="L"
                    i+=1
                    j-=1
            elif(l[i]=="L" and l[j]=="L"):
                j-=1
                while(i<j):
                    l[j]="L"
                    j-=1
            elif(l[i]=="R" and l[j]=="R"):
                i+=1
                while(i<j):
                    l[i]="R"
                    i+=1