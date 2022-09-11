from queue import PriorityQueue
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        obj=PriorityQueue()
        arr=[[efficiency[i],speed[i]] for i in range(n)]
        arr.sort(reverse=True)
        # print(arr)
        ts=0
        INT_MAX=(10**9)+7
        ans=0
        for i in range(n):
            eff,curr_speed=arr[i]
            obj.put(curr_speed)
            if(i<k):
                ts+=curr_speed
            else:
                ts+=(curr_speed-obj.get())
            # print(ts)
            ans=max(ans,ts*eff)
        return ans%(INT_MAX)
        # # print(arr)
        # ans=0
        # for i in range(k):
        #     ans+=arr[i][0]
        #     obj.put(arr[i][::-1])
        # i+=1
        # result=0
        # # print(i)
        # while(i<n):
        #     a=arr[i]
        #     b=obj.get()
        #     if(obj.empty()):
        #         c=[INT_MAX,0]
        #     else:
        #         c=obj.get()
        #     s1=(ans*b[0])
        #     s2=((ans-b[1]+a[0])*(min(c[0],a[1])))
        #     if(s1<s2):
        #         ans=(ans-b[1]+a[0])
        #         obj.put(a[::-1])
        #     else:
        #         obj.put(b)
        #     if(c[0]!=INT_MAX):
        #         obj.put(c)
        #     i+=1
        # while(not obj.empty()):
        #     a=obj.get()
        #     result=max(result,(ans*a[0])%INT_MAX)
        #     ans-=a[1]
        # # return result%(INT_MAX+7)
        # return result%(INT_MAX)