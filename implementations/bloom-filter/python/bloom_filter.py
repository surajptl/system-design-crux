import random
#install murmurhash3
# pip install mmh3
import mmh3

class BloomFilter:
    """
    Basic Bloom Filter Implementation
    --------------------------
    A Bloom Filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set.
    It can yield false positives, but never false negatives.
    This implementation uses multiple hash functions to set bits in a bit array.
    The size of the bit array and the number of hash functions can be configured.
    Attributes:
        size (int): The size of the bit array.
        hash_count (int): The number of hash functions to use.
    """
    def __init__(self, size=1024, hash_count=8):
        if size < 1:
            raise ValueError("Size cannot be less than 1")
        if hash_count < 1:
            raise ValueError("Hash count cannot be less than 1")
        if hash_count > size:
            raise ValueError("Hash count cannot be greater than size")
        self._size = size
        self._hash_count = hash_count
        self._bit_array = self._create_storage()
        self._seed = [random.getrandbits(32) for _ in range(hash_count)]

    def _create_storage(self):
        """
        Create a bit array of the specified size.
        :return: A list of booleans initialized to False.
        """
        # Using a list of booleans to represent the bit array
        return [False] * self._size

    @property
    def size(self):
        return self._size
    
    @property
    def hash_count(self):
        return self._hash_count

    def _get_indices(self, item):
        """Hash the item using multiple hash functions.
        :param item: The item to hash.
        :return: A list of indices in the bit array.
        """
        # Using mmh3 to hash the item with different seeds
        s = str(item)
        return [mmh3.hash(s, seed) % self._size for seed in self._seed]

    def add(self, item):
        """Add an item to the Bloom filter.
        :param item: The item to add.
        """
        # Set the bits at the indices returned by the hash functions to True
        for index in self._get_indices(item):
            self._bit_array[index] = True

    def might_contain(self, item):
        """Check if the item might be in the Bloom filter.
        :param item: The item to check.
        :return: True if the item might be in the filter, False if it definitely is not.
        """
        # Check if all bits at the indices returned by the hash functions are True
        # If any bit is False, the item is definitely not in the filter
        return all(self._bit_array[index] for index in self._get_indices(item))
