class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for item in cpdomains:
            count,host=item.split()
            host=host.split(".")
            hosts=[]
            while(len(host)!=0):
                if(len(hosts)==0):
                    hosts.append(host.pop())
                else:
                    ans=f"{host.pop()}.{hosts[-1]}"
                    hosts.append(ans)
            for val in hosts:
                if(val in d):
                    d[val]+=int(count)
                else:
                    d[val]=int(count)
        ans=[]
        for item in d:
            ans.append(f"{d[item]} {item}")
        return ans
            