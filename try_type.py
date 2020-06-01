def try_int(val):
    """Returns whether an input variable can be cast to an integer"""
    try:
        int(val)
    except:
        return False
    return True
