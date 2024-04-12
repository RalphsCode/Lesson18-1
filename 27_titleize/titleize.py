def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    return phrase.title()

    """
    OR:
    
    capitalized = ''
    word_list = phrase.split(' ')
    for word in word_list:
        capitalized += (word[0:1].upper() + word[1:].lower()) +' '
    return capitalized.strip()
    """