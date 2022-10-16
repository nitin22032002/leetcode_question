class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        arr=list(binary)
        c=arr.count("0")
        i=0
        while(i<len(arr)-1):
            if(arr[i]=="0"):
                c-=1
                if(c==0):
                    i+=1
                    while(i<len(arr)):
                        arr[i]="1"
                        i+=1
                else:
                    arr[i]="1"
                    arr[i+1]="0"
            i+=1
        return "".join(arr)
            