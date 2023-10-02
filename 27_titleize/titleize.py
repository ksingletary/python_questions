def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    return ' '.join([s.capitalize() for s in phrase.split(' ')])


print(titleize('oNLy cAPITALIZe fIRSt'))