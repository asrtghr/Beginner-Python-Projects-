import random
import time

# Implementation of binary search algorithm!!
# If you have a sorted list and you want to search this array for something,
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(rn_iterable, target):
  for i in range(len(rn_iterable)):
      if rn_iterable[i] == target:
          return i
  return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(rn_iterable, target, low = None, high = None):
  if low is None:
    low = 0
  if high is None:
      high = len(rn_iterable) - 1

  if high < low:
      return -1

  middlepoint = (low + high) // 2

  if target == rn_iterable[middlepoint]:
    return middlepoint
  elif target < rn_iterable[middlepoint]:
    return binary_search(rn_iterable, target, low, middlepoint - 1)
  else:
    return binary_search(rn_iterable, target, middlepoint + 1, high)


# selecting only unique values
rn_iterable = set([random.randint(0,10000) for _ in range(1000)])
sorted_list = sorted(rn_iterable)

print(f"BINARY SEARCH: ")
start = time.time()
for target in sorted_list:
  binary_search(sorted_list, target)
end = time.time()
print("Binary search time: ", (end - start), "seconds")

print('\n')

print(f"NAIVE SEARCH: ")
start = time.time()
for target in sorted_list:
  naive_search(sorted_list, target)
end = time.time()
print("Naive search time: ", (end - start), "seconds")
