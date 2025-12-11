# [CPU (Catamount Processing Unit)](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/cs2210/cs2210home.md)
# CPU.py
>wires together the `ALU`, register file, data memory and instruction memory and implements a simple fetch–decode–execute cycle.
### `_fetch()`
>reads the instruction at PC into the instruction register `_ir` and then increments `_pc` by 1. 

That means after fetch the PC already points to the next instruction — useful for CALL which pushes the return address = current PC.

### `_decode()`
>Delegates decoding to an Instruction helper

>The CPU supports mnemonics such as `LOADI, LUI, LOAD, STORE, ADDI, ADD, SUB, AND, OR, SHFT, BEQ, BNE, B, CALL, RET, HALT`.

(Instruction(raw=self._ir)), and the execute phase is implemented with a match on the decoded mnemonic. 

### Branching --> `BEQ` `BNE` `B`
>BEQ and BNE consult self._alu.zero to decide whether to take a branch — i.e., branch decisions rely on flags set by previous ALU operations. B always branches. Offsets are sign-extended before adding to PC.

### Memory ops / stack `LOAD` `STORE` `CALL` `RET` 
- `LOAD` computes an address `val_a + imm` (with sign-extension) and reads from data memory. 
- `STORE` computes the same and writes to data memory (after enabling write). 
- `CALL` decrements the stack pointer `_sp`, writes the return address into data memory with `from_stack=True` and jumps to the target.
- `RET` reads the return address from memory (again using from_stack semantics) increments `_sp`, and loads `PC`.

### sext(value, bits=16)
>is a helper that sign-extends a bits-wide value to a Python int (two’s complement).

### Instruction & program loading
>load_program(prog) calls into InstructionMemory.load_program so the instruction memory is written once before execution begins.

Program loading is performed by make_cpu(prog) when given a program.

### `memory.py` — instruction vs data memory (Harvard)
- There are two memory types: `InstructionMemory` and `DataMemory`, both derived from Memory. The simulator uses **Harvard** architecture (separate instruction and data spaces)
- is word-addresable and sparse: _cells is a dict mapping addresses → 16-bit words; default returns 0 for unread cells. _check_addr enforces valid address range (0..65535). read(addr) returns stored value or default. write() only works if _write_enable is True. After a successful write the implementation clears _write_enable.

### `Register_File.py`
> There are 8 general-purpose registers implemented by RegisterFile (R0–R7). Each Register stores a value and exposes .raw to get the unsigned 16-bit representation.
- RegisterFile.execute(...) is the single API used by the CPU:
    - If write_enable=True it calls _write(rd, data) which validates rd and data (raises TypeError for missing args) and then writes into the chosen register.
    - If write_enable=False it calls _read(ra, rb) which returns (val_ra, val_rb_or_None). Reading rules: ra must be supplied, rb optional; if both missing an error is raised.  The CPU expects a tuple from reads and indexes the returned values appropriately.
    - 
### `ALU.py`
 - The ALU supports these operations: `ADD, SUB, AND, OR, SHFT`. You can set the operation with `set_op(op)` and then call `execute(a,b)`. execute clears flags, runs the operation, then returns the signed result (two’s complement) `via_to_signed()`. Flags are stored `in_flags`.
- **Flags:**
  - **N** (negative) — set if MSB of result is 1 (i.e., result is negative in two’s complement).
  - **Z** (zero) — set if result == 0.
  - **C** (carry) — for add: set if addition overflowed past 16 bits; for sub: set if minuend >= subtrahend (ARM-like semantics); for shifts: carry is last bit shifted out (special-case shift-by-zero leaves carry unchanged).
  - **V** (overflow) — set on signed arithmetic overflow (checked using sign bits).
