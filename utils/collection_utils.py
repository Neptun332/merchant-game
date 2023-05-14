from typing import TypeVar, List

T = TypeVar('T')


def get_single(collection: List[T]) -> T:
    if len(collection) > 1:
        raise ValueError(f"Expected single element collection, got multiple objects in list")

    if len(collection) == 0:
        raise ValueError(f"Expected single element collection, got empty collection")

    return collection[0]


