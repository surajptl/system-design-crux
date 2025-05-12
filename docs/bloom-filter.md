
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

- 📘 [Wikipedia: Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter)
- 📄 [Bloom Filters - MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-6-hashing-and-bloom-filters/)
- 🧠 [Bloom Filters by Jeff Dean (Google)](https://www.youtube.com/watch?v=4SK0yZ9de3M)
- 📚 [Probabilistic Data Structures for Web Analytics](https://engineering.linkedin.com/blog/2016/02/bloom-filters---the-whys--whats-and-hows)
- 🔍 [Cloudflare: How Bloom Filters Help Block Bots](https://blog.cloudflare.com/counting-things-a-lot-of-things/)

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
