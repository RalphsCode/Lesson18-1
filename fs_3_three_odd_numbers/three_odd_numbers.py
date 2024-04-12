def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    sum = 0
    for index, val in enumerate(nums):
        if len(nums[index:]) <= 2:
               print('Reached end of list.')
               return False
        sum = val + nums[(index+1)] + nums[(index+2)]
        print('currently processing', val, nums[(index+1)], nums[(index+2)])
        if sum % 2 == 1:
            print('Found odd sum:', val, nums[(index+1)], nums[(index+2)])
            return True
        sum = 0
        
    return False
