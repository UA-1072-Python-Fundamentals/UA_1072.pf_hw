__all__ = ['search_letters']


def search_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    result = set(letters).intersection(set(phrase))
    return '-' if result == set() else result