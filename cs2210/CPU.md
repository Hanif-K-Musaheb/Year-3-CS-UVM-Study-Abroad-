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
LOAD computes an address val_a + imm (with sign-extension) and reads from data memory. STORE computes the same and writes to data memory (after enabling write). CALL decrements the stack pointer _sp, writes the return address into data memory with from_stack=True and jumps to the target. RET reads the return address from memory (again using from_stack semantics) increments _sp, and loads PC.
