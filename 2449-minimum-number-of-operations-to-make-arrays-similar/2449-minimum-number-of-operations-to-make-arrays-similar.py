from sortedcontainers import SortedList
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        odd=SortedList()
        even=SortedList()
        opt=[]
        i=0
        j=0
        while(i<len(nums) and j<len(target)):
            if(nums[i]==target[j]):
                i+=1
                j+=1
            elif(nums[i]>target[j]):
                opt.append(target[j])
                j+=1
            else:
                if(nums[i]%2==0):
                    even.add(nums[i])
                else:
                    odd.add(nums[i])
                i+=1
        while(i<len(nums)):
            if(nums[i]%2==0):
                    even.add(nums[i])
            else:
                    odd.add(nums[i])
            i+=1
        while(j<len(target)):
            opt.append(target[j])
            j+=1
        ans=0
        # print(opt,even,odd)
        for item in opt:
            if(item%2==0):
                lower=even.bisect_left(item)
                # print(lower)
                if(lower==0):
                    cost=(even[lower]-item)//2
                    # ans+=cost
                    even.discard(even[lower])
                else:
                    cost=(item-even[lower-1])//2
                    even.discard(even[lower-1])
                # else:
                #     a1=(item-even[lower-1])//2
                #     a2=(even[lower]-item)//2
                #     print("-",a1,a2)
                #     if(a1<=a2):
                #         even.discard(even[lower-1])
                #         cost=a1
                #     else:
                #         even.discard(even[lower])
                #         cost=a2
                ans+=cost
                # print(cost,lower)
            else:
                lower=odd.bisect_left(item)
                # print(lower)
                if(lower==0):
                    ans+=(odd[lower]-item)//2
                    odd.discard(odd[lower])
                else:
                    ans+=(item-odd[lower-1])//2
                    odd.discard(odd[lower-1])
                # else:
                #     a1=(item-odd[lower-1])//2
                #     a2=(odd[lower]-item)//2
                #     if(a1<=a2):
                #         odd.discard(odd[lower-1])
                #         ans+=a1
                #     else:
                #         odd.discard(odd[lower])
                #         ans+=a2
        return ans//2