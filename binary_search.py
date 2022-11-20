import random

# Implementation of binary search algorithm!!
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(rn_iterable, target):
  for element in rn_iterable:
    if element == target:
      return element
  return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(rn_iterable, target, low = None, high = None):
  low = 0 if not low else low
  high = len(rn_iterable) - 1 if not high else high

  middlepoint = (low + high) // 2
  # we'll check if rn_iterable[middlepoint] == target, and if not, we can find out if
  # target will be to the left or right of middlepoint
  # we know everything to the left of midpoint is smaller than the middlepoint
  # and everything to the right is larger
  if target == rn_iterable[middlepoint]:
    print(target)
  elif target < rn_iterable[middlepoint]:
    return binary_search(rn_iterable, target, low, middlepoint-1)
  else:
    return binary_search(rn_iterable, target, middlepoint+1, high)


# selecting only unique values
rn_iterable = set([random.randint(0,10000) for _ in range(1000)])
sorted_iterable = sorted(rn_iterable)

rn_choice = random.choice(sorted_iterable)

print(f"BINARY SEARCH: ")
%time
binary_search(sorted_iterable, rn_choice)

print('\n')

print(f"NAIVE SEARCH: ")
%time
naive_search(sorted_iterable, rn_choice)
