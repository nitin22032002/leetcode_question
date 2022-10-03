class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d=set()
        for item in emails:
            s=[]
            isAdd=False
            isPlus=False
            for val in item:
                if(val=="+" and not isAdd):
                    isPlus=True
                elif(val=="@"):
                    s.append(val)
                    isAdd=True
                    isPlus=False
                elif(not isPlus and (val!="." or isAdd)):
                    s.append(val)
            s="".join(s)
            d.add(s)
        return len(d)
                
                