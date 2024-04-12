def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    updated_letters_str = ''
    
    # seperate the letters in the phrase
    for letter in phrase:
        # letters match and are same case
        if letter == to_swap:
            if to_swap.islower():
                updated_letters_str += letter.upper()
            else:
                updated_letters_str += letter.lower()
                
        # letters match but are different case
        elif letter == to_swap.upper() :
            updated_letters_str += letter.lower()
        elif letter == to_swap.lower() :
            updated_letters_str += letter.upper()            
        # if letter does not match, put it in list as is    
        else:
            updated_letters_str += letter
            
    ''' Did not know about switchcase() method 
        until I checked the springboard solution!'''
            
    return updated_letters_str