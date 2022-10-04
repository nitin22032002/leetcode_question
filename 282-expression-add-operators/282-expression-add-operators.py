class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if(int(num)==target and target!=0):
            return [num]
        elif(int(num)<target):
            return []
        return self.get(num,target,0,0,"+",0)
    def get(self,num,target,i,prvO,prvOp,exp):
        if(i>=len(num)):
            # if(exp==0):
            #     print(prvO,prvOp)
            exp=exp+prvO
            # print(exp)
            if(exp==target):
                return [""]
            else:
                return []
        else:
            j=i
            s=0
            ans=[]
            x=""
            while(j<len(num)):
                s=(s*10)+int(num[j])
                x+=num[j]
                if(prvOp=="*"):
                    e=prvO*s
                elif(prvOp=="-"):
                    e=s*-1
                else:
                    e=s
                if(j+1<len(num)):
                    for operator in ["+","-","*"]:
                        if(operator!="*"):
                            e1=exp+e
                            a=self.get(num,target,j+1,0,operator,e1)
                        else:
                            a=self.get(num,target,j+1,e,"*",exp)
                        for item in a:
                            if(len(item)!=0):
                                ans.append(x+operator+item)
                            else:
                                ans.append(x)
                else:
                    e1=exp+e
                    a=self.get(num,target,j+1,0,"+",e1)
                    for item in a:
                        if(len(item)!=0):
                            ans.append(x+operator+item)
                        else:
                            ans.append(x)
                    
                if(num[i]=="0"):
                    break
                j+=1
            return ans