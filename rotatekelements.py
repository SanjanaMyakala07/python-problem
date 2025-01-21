def rotate(nums, k):
    n = len(nums)
    k = k % n  
    reverse(nums, 0, n - 1)  
    reverse(nums, 0, k - 1)  
    reverse(nums, k, n - 1)  

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]  
        start += 1
        end -= 1
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  
