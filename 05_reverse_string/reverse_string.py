def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # new_str = ""
    # ourlist = list(phrase)
    # ourlist.reverse()

    # for letter in ourlist:
    #     new_str += letter

    # return new_str 

    # just rememberd slicing!

    return phrase[::-1]
print(reverse_string('awesome'))