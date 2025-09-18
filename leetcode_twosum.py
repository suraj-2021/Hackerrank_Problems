class Solution:
    def twoSum(nums,target):
        for i in range(0,len(nums)+1):
            j = i+1
            while(j<len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j] 
                
                j+=1   

nums = [3,2,4] 
target = 6

print(Solution.twoSum(nums,target))

