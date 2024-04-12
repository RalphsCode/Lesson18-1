def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letters_list = [l for l in phrase]
    count = len(letters_list) -1
  
    reversed_list = []
    i = 0
    while i <= count:
        reversed_list.append(letters_list.pop())
        i +=1
    word_reversed = ''.join(reversed_list)
    return word_reversed

reverse_string('hplaR')