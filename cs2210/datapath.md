# [Datapath](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/cs2210/cs2210home.md)
## Datapath & CPU Control — The Big Picture
> The datapath is the part of the CPU where actual data processing happens.

>The CPU control unit decides how the datapath is used for each instruction. It generates control signals that tell each component what to do.


### 1. Instruction Fetch
>Instruction fetch is the same for every instruction.


##### Key steps

1. PC → Instruction Memory
     - The **Program Counter** (PC) holds the address of the next instruction.
     - **Control signals** tell instruction memory to read the instruction at **PC**.
2. Instruction Memory → Instruction Register (IR)
     - The fetched instruction is stored temporarily for decoding.
3. PC Update
    - In simple datapaths, PC = PC + 4 (assuming 32-bit instructions)
    - For **jumps/branches**, this may change later.

##### Datapath components used
 - Program Counter (PC)
 - Instruction Memory
 - Adder (for PC + 4)
 - MUX (to choose next PC in case of branch/jump)


### 2. ALU Operations
These occur for instructions like:
 - Arithmetic: add, sub, addi
 - Logical: and, or, xor
 - Address calculation: used by loads/stores

##### Key steps
1. Read operands
   - The register file outputs two values:
   - Read register 1
   - Read register 2 or immediate (immediate is just a raw value)
2. Select input to ALU
    - A MUX chooses between:
      - Second register value
      - Immediate value
3. ALU computes result
    - The ALU control (a sub-unit of CPU control) decides the ALU function:
      - add, subtract, and, or, slt, etc.

4. Write result back
    - If the instruction writes to a register, the result goes to the register file.
      
### 3. Memory Operations
These are for:
 - **Load** instructions
 - **Store** instructions
###### For Load 
 - Compute address (ALU)
     - address = base register + offset
 - Read from data memory
     - Data Memory[address] → output
 - Write data into register file
###### For Store 
 - Compute address
 - Write data memory
     - Data Memory[address] = value from register file
 - No register writeback

### The control unit generates signals that orchestrate everything.
It decides:
 - What the ALU should do (ALU control)
 - Whether memory is doing a read or write
 - Whether a value should be stored into the register file
 - Which MUX inputs to select (e.g., ALU input from register or immediate)



# Summary Cheat Sheet
### Summary Cheat Sheet
 - Instruction Fetch
     - Read instruction from memory using PC
     - Update PC (usually PC + 4)
 - ALU Operations
     - Read operands from register file
     - ALU computes arithmetic/logical result
     - Write result to register (if needed)
 - Memory Operations
     - ALU computes address
     - Load → read data memory → write register
     - Store → write data memory
 - Control Unit
     - Decodes instruction
     - Generates control signals for ALU, memory, registers, MUXes
     - Ensures datapath follows correct sequence for each instruction
