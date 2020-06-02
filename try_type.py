# Module for trying to parse values as types

def try_str(val):
    """Returns whether an input value can be cast to a string"""
    try:
        str(val)
    except:
        return False
    return True

def try_float(val):
    """Returns whether an input value can be cast to a float"""
    try:
        float(val)
    except:
        return False
    return True

def try_int(val):
    """Returns whether an input value can be cast to an integer"""
    try:
        int(val)
    except:
        return False
    return True
