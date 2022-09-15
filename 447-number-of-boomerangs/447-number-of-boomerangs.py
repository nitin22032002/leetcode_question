class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)):
            d={}
            for j in range(len(points)):
                if(i==j):
                    continue
                x1,y1=points[i]
                x2,y2=points[j]
                dis=self.distance(x1,x2,y1,y2)
                # print(dis)
                # print(dis)
                if(dis in d):
                    d[dis]+=1
                else:
                    d[dis]=1
            # print(d)
            for item in d:
                if(d[item]>=2):
                    n=d[item]
                    ans+=((((n)*(n-1)))//2)*(2)
        return ans
            
    def distance(self,x1,x2,y1,y2):
        # print((x1,y1),(x2,y2))
        return pow(x1-x2,2)+pow(y2-y1,2)