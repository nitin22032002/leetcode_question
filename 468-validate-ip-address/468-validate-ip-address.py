class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if("." in queryIP):
            if(self.validateIpv4(queryIP)):
                return "IPv4"
        elif(":" in queryIP):
            if(self.validateIpv6(queryIP)):
                return "IPv6"
        return "Neither"
    def validateIpv4(self,ip):
        arr=ip.split(".")
        if(len(arr)!=4):
            return False
        for item in arr:
            if(not self.validNumber(item)):
                return False
        return True
    def validNumber(self,n):
        num=0
        if(len(n)==0):
            return False
        if(len(n)>=2):
            if(n[0]=="0"):
                return False
        for item in n:
            if(item>='0' and item<='9'):
                num=(num*10)+int(item)
            else:
                return False
        if(num<=255):
            return True
        return False
    def validateIpv6(self,ip):
        arr=ip.split(":")
        if(len(arr)!=8):
            return False
        for item in arr:
            if(not self.valid(item)):
                return False
        return True
        
    def valid(self,s):
        if(len(s)>4 or len(s)==0):
            return False
        for item in s:
            if((item>='a' and item<='f') or (item>='A' and item<='F') or (item>='0' and item<='9')):
                continue
            return False
        return True
        
            