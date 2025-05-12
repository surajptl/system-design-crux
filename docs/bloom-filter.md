
# 🌸 Bloom Filter - System Design Crux

## 📘 What is a Bloom Filter?

A **Bloom Filter** is a space-efficient probabilistic data structure used to test whether an element is a member of a set.

- **Use case**: Checking membership quickly (e.g., “Have we seen this item before?”).
- **Advantage**: Very memory efficient.
- **Trade-off**: It can return **false positives** (says an item is present when it is not), but **never false negatives** (never says an inserted item is absent).

## ⚙️ Key Characteristics

| Property            | Value                    |
|---------------------|---------------------------|
| False Positives     | ✅ Possible               |
| False Negatives     | ❌ Never                  |
| Space Efficiency    | ✅ High                   |
| Speed               | ✅ Very Fast              |

---

## 🔍 How It Works

1. A bit array of size `m` is initialized to all `0`s.
2. `k` independent hash functions are used.
3. To insert an item:
   - Hash it `k` times.
   - Set bits at the resulting indices to `1`.
4. To check for membership:
   - Hash the item `k` times.
   - If **all bits** at the corresponding indices are `1`, it *might* be in the set.
   - If **any bit** is `0`, it's *definitely not* in the set.

---

## 📦 Example Use Cases

- Web caches (e.g., Chrome’s Safe Browsing)
- Databases to check non-existence before querying disk
- Distributed systems like Cassandra, HBase
- Bitcoin and blockchain filters
- Spam filters and password breach checks

---

## 🛠 Implementation Details

This implementation is in **Python**, using:
- A boolean list to simulate a bit array
- `mmh3` (MurmurHash3) for fast hashing
- Random seeds to generate multiple hash functions

### 🧪 File Structure

```
system-design-crux/
│
├── bloom_filter/
│   ├── bloom_filter.py       # Core BloomFilter class
│   ├── test_bloom_filter.py  # Unit tests using pytest
│
├── docs/
│   └── bloom_filter.md       # This documentation
```

---

## 🔗 References & Further Reading

- 📖 [Wikipedia: Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter)
- 📖 [The Case for Learned Index Structures](https://doi.org/10.1145/3183713.3196909)
- 📖 [Bloom filters - introduction and implementation](https://www.google.com/search?q=https://www.geeksforgeeks.org/bloom-filters-introduction-and-implementation/)
- 📖 [A model for learned bloom filters, and optimizing by sandwiching](https://www.google.com/search?q=https://proceedings.neurips.cc/paper/2018/hash/58355a0432f0207a5b2338ad17f80c1a-Abstract.html)
- 📖 [On the false-positive rate of Bloom filters](https://doi.org/10.1016/j.ipl.2008.05.018)
- 📖 [Adaptive Learned Bloom Filter (Ada-BF): Efficient Utilization of the Classifier](https://doi.org/10.48550/arXiv.1910.09131)
- 📖 [Partitioned Learned Bloom Filter](https://www.google.com/search?q=https://doi.org/10.48550/arXiv.2006.03176)
- 📖 [Stable learned bloom filters for data streams](https://doi.org/10.14778/3407790.3407830)
- 📖 [Approximately detecting duplicates for streaming data using stable bloom filters](https://doi.org/10.1145/1142473.1142477)
- 📖 [Bloom Filters Explained](https://systemdesign.one/bloom-filters-explained/)
- 📖 [Redis Bloom Filter Documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter/)

---

## 💻 Language & Tools

- **Language**: Python 3.8+
- **Hashing Library**: [`mmh3`](https://pypi.org/project/mmh3/)
- **Testing Framework**: [`pytest`](https://docs.pytest.org/en/stable/)

---

## 🧪 Running the Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:
```
mmh3
```

### 2. Run the tests using `python`
```bash
python bloom_filter/test_bloom_filter.py
```

---

## ✅ Coming Up (Future Enhancements)

- Counting Bloom Filters
- Scalable Bloom Filters
- Compressed Bloom Filters
- Language support: Java, Go, Rust, C++
