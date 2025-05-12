
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


---

## 🔗 References & Further Reading

- 📖 [Wikipedia: Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter)
- 📖 [Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean, and Neoklis Polyzotis. 2018. The Case for Learned Index Structures. In Proceedings of the 2018 International Conference on Management of Data (SIGMOD '18). Association for Computing Machinery, New York, NY, USA, 489–504.](https://dl.acm.org/doi/10.1145/3183713.3196909)
- 📖 [Bloom filters - introduction and implementation. GeeksforGeeks. (2022, April 21)](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)
- 📖 [Michael Mitzenmacher. 2018. A model for learned bloom filters, and optimizing by sandwiching. In Proceedings of the 32nd International Conference on Neural Information Processing Systems (NIPS'18). Curran Associates Inc., Red Hook, NY, USA, 462–471](https://proceedings.neurips.cc/paper/2018/file/0f49c89d1e7298bb9930789c8ed59d48-Paper.pdf)
- 📖 [Prosenjit Bose, Hua Guo, Evangelos Kranakis, Anil Maheshwari, Pat Morin, Jason Morrison, Michiel Smid, Yihui Tang. 2008. On the false-positive rate of Bloom filters. Information Processing Letters, Volume 108, Issue 4, 2008, Pages 210-213, ISSN 0020-0190.](https://www.sciencedirect.com/science/article/abs/pii/S0020019008001579)
- 📖 [Zhenwei Dai, Anshumali Shrivastava. 2019. Adaptive Learned Bloom Filter (Ada-BF): Efficient Utilization of the Classifier. Computing Research Repository (CoRR '20).](https://arxiv.org/abs/1910.09131)
- 📖 [Kapil Vaidya, Eric Knorr, Tim Kraska, Michael Mitzenmacher. 2020. Partitioned Learned Bloom Filter. Computing Research Repository (CoRR '20).](https://arxiv.org/abs/2006.03176)
- 📖 [Qiyu Liu, Libin Zheng, Yanyan Shen, and Lei Chen. 2020. Stable learned bloom filters for data streams. Proc. VLDB Endow. 13, 12 (August 2020), 2355–2367. ](https://dl.acm.org/doi/10.14778/3407790.3407830)
- 📖 [Fan Deng and Davood Rafiei. 2006. Approximately detecting duplicates for streaming data using stable bloom filters. In Proceedings of the 2006 ACM SIGMOD international conference on Management of data (SIGMOD '06). Association for Computing Machinery, New York, NY, USA, 25–36](https://dl.acm.org/doi/10.1145/1142473.1142477)
- 📖 [Bloom Filters Explained](https://systemdesign.one/bloom-filters-explained/)
- 📖 [Redis Bloom Filter Documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter/)
