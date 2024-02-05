#!/usr/bin/env python3
"""LFUCache module"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    least_frequent_keys = [k for k, v in self.frequency.items() if v == self.min_frequency]
                    if least_frequent_keys:
                        least_recently_used = min(self.queue, key=self.queue.index)
                        least_frequent_and_recent = [k for k in least_frequent_keys if k in self.queue]
                        key_to_discard = least_recently_used if least_recently_used in least_frequent_and_recent else least_frequent_keys[0]
                        del self.cache_data[key_to_discard]
                        del self.frequency[key_to_discard]
                        self.queue.remove(key_to_discard)
                        print("DISCARD:", key_to_discard)
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_frequency = 1
                self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    my_cache = LFUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
