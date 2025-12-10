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

- **LRU** - Least Recently Used (in terms of caches)
    - LRU is a replacement algorithm used when the cache is full and a new block needs to be loaded. It chooses to evict the block that has not been used for the longest time.
 - A recent bit (rent bit) is:
    - A bit that tells the cache controller whether a cache entry has been used recently.
    - An entry may only be evicted if its recent/rent bit is 0.


Intuition:

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

# Registers and register file
## Registers
##### Properties:
 - Accessed in one clock cycle
 - Used for operands, addresses, and intermediate values
 - Very small number (e.g., 16–32 registers in typical ISAs, 128+ in SIMD)

## Register File
A register file is a small, fast storage structure containing all registers used by the processor.
#### A register file typically includes:
 - A fixed number of registers (e.g., 32 × 32-bit)
 - Read ports (for reading operands)
 - Write ports (for writing results)
 - Decoders, multiplexers, and control logic

#### Construction of a Register File:
###### A register file consists of:
1. An array of registers
2. **Decoders**
       - **Read** decoders: select which register(s) will be read
       - **Write** decoder: selects which register will be written
3. **Read Ports**
       - A decoder (selects register)
       - A large Multiplexer (MUX) that chooses output from one of many registers
4. **Write Port**
       - A decoder that activates the selected register
       - A write-enable line
       - The data to write
5. **Clock and control signals**
       - All writes happen on the clock edge.
###### Multi-Port Register File
>A multi-port register file provides multiple independent read and write ports.
    

## Summary Table
| Term                    | Meaning                                                   | Impact                              |
| ----------------------- | --------------------------------------------------------- | ----------------------------------- |
| **Hit**                 | Data is found in the mapped cache line (tag matches)      | Very fast access                    |
| **Miss**                | Data is NOT in the mapped cache line                      | Must fetch from slower memory       |
| **Miss Penalty**        | Extra time to fetch data from lower memory and load cache | Slows program execution             |
| **Direct-Mapped Cache** | Each memory block can go to only one cache line           | Simple but prone to conflict misses |

| Term               | Meaning                              | Why It Matters                           |
| ------------------ | ------------------------------------ | ---------------------------------------- |
| **Register**       | Small, fast CPU storage              | Holds operands for instructions          |
| **Register File**  | Array of all CPU registers           | Supports multiple reads/writes per cycle |
| **Read Port**      | Hardware path to read a register     | Allows parallel operand reads            |
| **Write Port**     | Hardware path to write a register    | Allows results to be written             |
| **Decoder**        | Selects which register to read/write | Core of register file access             |
| **Multi-Port**     | Multiple simultaneous reads/writes   | Enables parallel execution               |
| **RAW Hazard**     | Read occurs before write completes   | Solved via forwarding/bypassing          |
| **Write Conflict** | Two write ports target same register | Solved by priority logic                 |
