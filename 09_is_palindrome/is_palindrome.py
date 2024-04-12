def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    original_letters = []
    for letter in phrase.lower().replace(" ", "") :
        original_letters.append(letter)
     
    print(f'Original Letters: {original_letters}')
    
    backwards_letters = original_letters[::-1]
    
    print(f'Backwards Letters: {backwards_letters}')
    
    if original_letters == backwards_letters:
        return True
    else:
        return False
