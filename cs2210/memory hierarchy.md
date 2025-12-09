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


## Hits, misses, and penalties
