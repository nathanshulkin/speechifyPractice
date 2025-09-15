#!/usr/bin/env python3
from typing import Any, Optional

class LRUCache:
    """
    A Least Recently Used (LRU) cache keeps items in the cache until it reaches its size
    and/or item limit (only item in our case). In which case, it removes an item that was accessed
    least recently.
    An item is considered accessed whenever `has`, `get`, or `set` is called with its key.

    Implement the LRU cache here and use the unit tests to check your implementation.
    """

    def __init__(self, item_limit: int):
        self.this = {}
        self.item_limit = item_limit
        print("howdy doody")

    def has(self, key: str) -> bool:
        if key not in self.this:
            return False
        else:
            return True

    def get(self, key: str) -> Optional[Any]:
        if key in self.this:
            return self.this[key]
        else:
            return None

    def set(self, key: str, value: Any):
        # TODO: implement this function
        if len(self.this) == self.item_limit:
            print(self.this)
            for x in self.this:
                print(x)
                print(self.this[x])
                # self.this.update({x: self.this[x]})
            self.this.popitem()
            print(self.this)
        self.this.update({key: value})
