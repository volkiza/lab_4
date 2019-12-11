class ListLenError(Exception):
    pass


class LargeSampleError(Exception):
    pass


def s_mean(nums):
    try:
        n = max(len(nums),1)
        if n<2:
            raise ListLenError()
        return float(sum(nums)) / n
    except ValueError:
        print("Enter numerical values, wrong value entered")        
    except ListLenError:
        print("Enter more than one number")
        

def s_median(nums):
    n = len(nums)
    try:
        if n<2:
            raise ListLenError()
    except ListLenError:
        print("Enter more than one number")        
    nums.sort()
    try:
        if n % 2 == 0:
            med1 = nums[n // 2]
            med2 = nums[n // 2 - 1]
            med = (med1 + med2) / 2
        else:
            med = nums[n // 2]
    except ValueError:
        print("Enter numerical values, wrong value entered")
    return med


def s_var(nums):
    tot = 0
    try:
        for i in nums:
            tot += (s_mean(nums) - i) ** 2
    except ValueError:
        print("Enter numerical values, wrong value entered")
    variance = tot / len(nums)
    return variance


def sample_var(nums):
    tot = 0
    try:
        for i in nums:
            tot += (s_mean(nums) - i) ** 2
        n = (len(nums)-1) 
    except ValueError:
        print("Enter numerical values, wrong value entered")
    try:
        if n>5000:
            raise LargeSampleError()
    except LargeSampleError:
        print("Enter less than 5001 observations to be considered a sample") 
    
    variance = tot / n
    return variance


def s_std(nums):
    return s_var(nums)**0.5


def sample_std(nums):
    return sample_var(nums)**0.5
