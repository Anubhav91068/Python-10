

def stats(nums):
    smallest = min(nums)
    largest = max(nums)
    average = sum(nums) / len(nums)

    return (smallest, largest, average)

nums = list(map(int, input().split()))

print(stats(nums))