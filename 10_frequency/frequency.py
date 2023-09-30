def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = 0
    for num in lst:
        if num == search_term:
            count += 1
        elif num not in lst:
            return 0
    return count

print(frequency([1, 4, 3,5,3,4,7,7,6,2,4,7,8,97,9,34], 7))