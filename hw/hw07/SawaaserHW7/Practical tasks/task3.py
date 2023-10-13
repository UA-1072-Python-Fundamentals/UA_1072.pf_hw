def count_characters(string: str) -> dict:
    """Calculates the number of characters included in given string
    Args:
        string: str
    Return:
        Dict with characters and how often they are in string"""
    d = {}
    for x in set(string):
        d[x] = string.count(x)
    return d


print(count_characters("hello"))