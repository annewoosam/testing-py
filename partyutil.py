"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if name and email are related to Mel.

    >>> is_mel('Mel Melitpolski', 'mel@ubermelon.com')
    True

    >>> is_mel('Mel Smith', 'mel@ubermelon.com')
    True

    >>> is_mel('Mel Melitpolski', 'totallynotmel@ubermel.com')
    True

    >>> is_mel('Jill', 'jill@ubermelon.com')
    False
    """

    return name == 'Mel Melitpolski' or email == 'mel@ubermelon.com'


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.]

# full list sample

    >>> treats = [{'type':'dessert'},{'type':'dessert'},{'type':'appetizer'},{'type':'dessert'},{'type':'appetizer'},{'type':'drink'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'drink')

# one item sample

    >>> treats = [{'type':'dessert'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'dessert')

# empty list Sample

    >>> treats = []
    >>> most_and_least_common_type(treats)
    (None, None)

# tie sample. Takes first item alphabetically in list if tie as tie-breaker.

    >>> treats = [{'type':'dessert'},{'type':'drinks'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'dessert')

    >>> treats = [{'type':'drinks'},{'type':'dessert'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'dessert')

    """

    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
