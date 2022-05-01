
def twoSum(nums: list, target: int):
  subdict = {}
  for i, num in enumerate(nums):
    if (target - num) in subdict:
      return i, subdict[target - num]
    else:
      subdict[num] = i

print(twoSum([3,2,4], 6)) 