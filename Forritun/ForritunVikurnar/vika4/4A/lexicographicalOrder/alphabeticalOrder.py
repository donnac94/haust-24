def precedes(first: str, second: str) -> str:
    """
    Returns the string that comes first in lexicographical order.
    """
    if first.lower() < second.lower():
        return first 
    else: return second
        