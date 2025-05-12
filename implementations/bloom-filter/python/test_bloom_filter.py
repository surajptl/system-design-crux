import unittest
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloom = BloomFilter(size=100, hash_count=5)

    def test_add_and_check_existing_item(self):
        self.bloom.add("apple")
        self.assertTrue(self.bloom.might_contain("apple"))

    def test_check_non_existing_item(self):
        self.bloom.add("apple")
        self.assertFalse(self.bloom.might_contain("banana"))  # Might fail on false positive

    def test_false_positive_rate(self):
        """This test checks for potential false positives but should not fail often."""
        self.bloom.add("apple")
        false_positives = 0
        trials = 1000
        for i in range(trials):
            item = f"nonexistent_{i}"
            if self.bloom.might_contain(item):
                false_positives += 1
        rate = false_positives / trials
        self.assertLess(rate, 0.1, "False positive rate is too high")

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            BloomFilter(size=0, hash_count=2)

    def test_invalid_hash_count(self):
        with self.assertRaises(ValueError):
            BloomFilter(size=10, hash_count=0)

    def test_hash_count_exceeds_size(self):
        with self.assertRaises(ValueError):
            BloomFilter(size=5, hash_count=10)


if __name__ == "__main__":
    unittest.main()
