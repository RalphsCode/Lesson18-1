def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
        
    # check if data structure is a dictionary
    is_dict = True if isinstance(collection, (dict)) else False
    
    if not is_dict:
        # process a start indicator; if one is present
        if not isinstance(collection, set):
            if start:
                collection = collection[start::]
                print('start index passed in, collection modified: ', collection)
                
        # search for the sought element in iterable data structures
        if sought in collection:
            return True
        # if not found, return False
        return False
    
    else:
        if sought in collection.values():
            return True
        else:
            return False