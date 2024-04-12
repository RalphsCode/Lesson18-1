def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    frequency_dict = dict()
    # loop thru the numbers and count frequency
    for el in nums:
        # put the counts in a dictionary
        frequency_dict[el] = nums.count(el)
    
    # locate the most frequent element
    highest_frequency = max(frequency_dict.values())
    
    # pull out the element that was most frequent
    for (el, freq) in frequency_dict.items():
        if freq == highest_frequency:
            print(f'Most frequent element is: {el}, which was included: {freq} times.')
            return el

mode(['hi', 'hello', 'hey', 'hi', 'what up', 'hi'])