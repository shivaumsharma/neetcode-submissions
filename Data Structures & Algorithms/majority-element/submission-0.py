class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        n=len(nums)
        for num in nums:
            count=(n/2)
            if num not in seen:
                seen[num]=1
            else: 
                seen[num]+=1
            if seen[num]>n/2:
                return num
            

