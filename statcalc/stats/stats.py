def s_mean(nums):
    return float(sum(nums)) / max(len(nums), 1)


def s_median(nums):
    n = len(nums)
    nums.sort()
    if n % 2 == 0:
        med1 = nums[n // 2]
        med2 = nums[n // 2 - 1]
        med = (med1 + med2) / 2
    else:
        med = nums[n // 2]
    return med


def s_var(nums):
    tot = 0
    for i in nums:
        tot += (s_mean(nums) - i) ** 2
    variance = tot / len(nums)
    return variance

def sample_var(nums):
    tot = 0
    for i in nums:
        tot += (s_mean(nums) - i) ** 2
    variance = tot / (len(nums)-1)
    return variance

def s_std(nums):
    return s_var(nums)**0.5

def sample_std(nums):
    return sample_var(nums)**0.5
