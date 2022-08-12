https://leetcode.com/problems/two-sum/



```
   my_nums= {}
        for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in my_nums:
               return [i, my_nums[remaining]]
            
           my_nums[value] = i 

```
