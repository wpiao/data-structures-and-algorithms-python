def binary_search(list, target):
    """
    binary_search function takes two parameters: a sorted list and the search key.
    In each search, it compares middle element of the list and the search key to eliminate half of the elements.
    It keeps doing it until it finds the search key and return its index. If it doesn't find the search key, it would return -1.
    """
    min = 0
    max = len(list) - 1
    while max >= min:
        mid = (min + max) // 2
        if list[mid] < target:
            min = mid + 1
        elif list[mid] > target:
            max = mid - 1
        else:
            return mid
    return -1
