# binary search requires sorted iterator. Common variation is find left-most or right-most index.
#
# Time:  O(log(n))
# Space: O(1)


# [lo, hi] version
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        # no overflow problem in python, (lo + hi) // 2 is better.
        # mid = lo + (hi - lo) // 2
        mid = (lo + hi) // 2
        '''
        change to your comparison condition as you need
        '''
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1


# [lo, hi) version
def binary_search2(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

# nums = [5,7,7,8,8,10], target = 8
# [5,7,7,8,8,10], 0-5, mid 2, retrieve mid right
# [8, 8, 10], 3-5, mid 4, retrieve mid right
# [8, 8], 3-4, mid 3, retrieve mid left
# return the left_most item equalling to the target
# result in [0, hi]
def bisect_left(arr, target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        # left-most, so equal will be on the right side
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
        '''
        # bisect right code
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
        '''
    return lo
