def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1 = {}
    list2 = {}
    for digit in str(num1):
        list1[digit] = list1.get(digit, 0) + 1
    for digit in str(num2):
        list2[digit] = list2.get(digit, 0) + 1

    return list1 == list2
print(same_frequency(551122, 221515))

