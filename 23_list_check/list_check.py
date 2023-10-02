def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    my_list = []
    for item in lst:
        if (isinstance(item, list)):
            my_list.append(item)
        if len(my_list) == len(lst):
            return True
    return False

print(list_check([[1], [2, 3]]))