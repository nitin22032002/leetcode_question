class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        arr=[]
        i=0
        n=""
        while(i<len(expression)):
            if(expression[i]>="0" and expression[i]<="9"):
                n+=expression[i]
            else:
                if(len(n)==0):
                    n="0"
                arr.append(n)
                arr.append(expression[i])
                n=""
            i+=1
        arr.append(n)
        return self.get(arr,0,len(arr)-1)
    def get(self,arr,start,end):
        # print(start,end)
        if(start==end):
            return [arr[start]]
        else:
            ans=[]
            i=start+1
            while(i<end):
                a=self.get(arr,start,i-1)
                b=self.get(arr,i+1,end)
                # print(a,b)
                for val1 in a:
                    for val2 in b:
                        ans.append(self.apply(val1,val2,arr[i]))
                i+=2
            return ans
    def apply(self,a,b,op):
        if(op=="*"):
            return int(a)*int(b)
        elif(op=="+"):
            return int(a)+int(b)
        else:
            return int(a)-int(b)
                