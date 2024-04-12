def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # if the first character in the string is a closing parentheses
    if parens[0] == chr(41):
        return False
    else:
        count = 0
        for el in parens:
            if el == chr(40):  # using ASCII code
                count += 1
            elif el == chr(41):
                count -= 1
                # if there is a closing parentheses that didn't get opened:
                if count < 0:
                    return False
        # check it all open parentheses are closed
        return count % 2 == 0