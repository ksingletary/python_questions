def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    my_list = []
    for char in a[0:2]:
        my_list.append(char)

    for char in b[0:2]:
        my_list.append(char)
        
    my_list.extend(a[2])
    my_list.extend(b[2])

    if len(set(my_list)) == len(my_list):
        return False
    return True
    

print(friend_date(('Elmo', 5, ['hugging', 'being nice']), ('Sauron', 5000, ['killing hobbits', 'chess'])))