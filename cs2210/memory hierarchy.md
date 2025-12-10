# [Memory Hierarchy](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/cs2210/cs2210home.md)
## Registers > L1 cache > L2 cache > L3 cache / SLC > RAM > non-volatile storage.
| Component                                    | Location                    | Speed                   | Size                       | Volatility       | Purpose / Notes                                                                            |
| -------------------------------------------- | --------------------------- | ----------------------- | -------------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| **Registers**                                | Inside the CPU core         | **Fastest**             | **Smallest** (bytes to KB) | Volatile         | Holds operands for the current instruction; directly accessed by the ALU.                  |
| **L1 Cache**                                 | Per CPU core                | Extremely fast          | Very small (16–128 KB)     | Volatile         | First-level cache; split into instruction (L1i) and data (L1d). Closest cache to the core. |
| **L2 Cache**                                 | Per core (usually)          | Very fast               | Medium (256 KB–2 MB)       | Volatile         | Second-level cache; larger and slightly slower than L1; reduces misses to L3.              |
| **L3 Cache / SLC (Shared Last-level Cache)** | Shared across all CPU cores | Fast                    | Large (4–64 MB or more)    | Volatile         | Final on-chip cache; improves inter-core communication and reduces RAM access.             |
| **RAM (Main Memory)**                        | On motherboard              | Much slower than caches | Very large (GBs)           | Volatile         | Stores active programs and data; accessed when not in CPU cache.                           |
| **Non-volatile Storage (SSD/HDD/NVMe)**      | Separate storage device     | Slowest                 | Huge (GB–TB)               | **Non-volatile** | Long-term storage for OS, apps, and files; loaded into RAM for execution.                  |

## Basics of direct-mapped caches
 - A direct-mapped cache is the simplest cache organization.
 - Each memory block can only go into exactly one specific cache line.

#### How a Direct-Mapped Cache Works
>A memory address is divided into three fields:

 - **Tag** – identifies which block is stored in the line
 - **Index** – selects the exact cache line
 - **Offset** – selects the byte/word inside that block
## Cache Hit
> A cache hit occurs when the CPU accesses an **address** and the data is already in the **cache line it maps to**.

##### Conditions for a hit:
 - The **correct** cache line is selected (based on index)
 - The tag **matches**
 - The valid bit is set

## Cache Miss
A cache miss happens when the data needed is **not** in the mapped cache line.
1. **Compulsory Miss** - The first time data is accessed (cold start). Cache has never seen it before.
1. **Conflict Mis**s - Two memory addresses map to the same cache line. Common in direct-mapped caches!
>Example: Address A and B both map to line 5. If CPU keeps switching between them → constant evictions → lots of misses.
3. **Capacity Miss** - The working set is bigger than the entire cache. Even if mapping is ideal, cache is just too small.

## Miss Penalty
When a miss happens, the CPU must fetch the block from lower-level memory:
- Often L2 or L3
- Or RAM if deeper caches also miss
#### Miss Penalty = extra time needed to fetch the block into the cache

## Summary Table
| Term                    | Meaning                                                   | Impact                              |
| ----------------------- | --------------------------------------------------------- | ----------------------------------- |
| **Hit**                 | Data is found in the mapped cache line (tag matches)      | Very fast access                    |
| **Miss**                | Data is NOT in the mapped cache line                      | Must fetch from slower memory       |
| **Miss Penalty**        | Extra time to fetch data from lower memory and load cache | Slows program execution             |
| **Direct-Mapped Cache** | Each memory block can go to only one cache line           | Simple but prone to conflict misses |
