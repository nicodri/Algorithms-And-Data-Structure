# Various sorting algorithms


# ### Quick sort: in place implementation, with two partition methods
def quick_sort(mylist):
    l = len(mylist)
    if l > 1:
        quick_sort_(mylist, 0, l - 1)


def quick_sort_(mylist, left, right):
    index = partition2(mylist, left, right)
    if left < index - 1:
        quick_sort_(mylist, left, index - 1)
    if right > index + 1:
        quick_sort_(mylist, index + 1, right)


def partition1(mylist, left, right):
    pivot = mylist[left]
    i = left + 1
    for j in xrange(left + 1, right + 1):
        if mylist[j] < pivot:
            temp = mylist[j]
            mylist[j] = mylist[i]
            mylist[i] = temp
            i += 1
    mylist[left] = mylist[i - 1]
    mylist[i - 1] = pivot
    print mylist
    print 'pivot is ', pivot
    print 'index is ', i - 1
    return i - 1


def partition2(mylist, left, right):
    pivot = mylist[(left + right) / 2]

    while left < right:
        # Find first element on left that should be on the right
        while mylist[left] < pivot:
            left += 1

        # Find last element on right that should be on the left
        while mylist[right] > pivot:
            right -= 1

        if left <= right:
            temp = mylist[left]
            mylist[left] = mylist[right]
            mylist[right] = temp

    print mylist
    print 'pivot is ', pivot
    print 'left is ', left
    return left


# ### Merge sort
def merge_sort(mylist):
    helper = [0]*len(mylist)
    return merge_sort_(mylist, helper, 0, len(mylist))


def merge_sort_(mylist, helper, low, high):
    if high - low > 1:
        middle = (low + high) / 2
        merge_sort_(mylist, helper, low, middle)
        merge_sort_(mylist, helper, middle, high)
        merge(mylist, helper, low, middle, high)


def merge(mylist, helper, low, middle, high):
    # Copying the original list
    for i in xrange(low, high):
        helper[i] = mylist[i]

    # Cursors
    left = low
    right = middle
    current = low

    while left < middle and right < high:
        if helper[left] < helper[right]:
            mylist[current] = helper[left]
            left += 1
        else:
            mylist[current] = helper[right]
            right += 1
        current += 1

    # Copy the remainder
    for i in xrange(left, middle):
        mylist[current] = helper[i]
        current += 1