# [FDE Cycle](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/cs2210/cs2210home.md)
## Instruction Register
**Definition**:
 - The Instruction Register (IR) is a CPU register that holds the current instruction being executed.

**Role in CPU operation**:
1. During the Fetch phase, the CPU fetches an instruction from memory (using the Program Counter).
2. That instruction is loaded into the Instruction Register.
3. The Control Unit then decodes the contents of the IR to generate control signals that drive the rest of the CPU (e.g., telling the ALU what to do).
   
| Aspect         | Description                        |
| -------------- | ---------------------------------- |
| Purpose        | Holds the current instruction      |
| Controlled by  | Control Unit                       |
| Updated during | Fetch cycle                        |
| Used for       | Instruction decoding and execution |


## Stack Frame
**Definition**:
A stack frame is a block of memory on the call stack that stores data for a single function (or subroutine) call.

Each time a function is called:
 - A new stack frame is created (pushed onto the stack).
 - When the function ends, that frame is **popped off**.

##### Contents of a Stack Frame
| Item                    | Purpose                                                                 |
| ----------------------- | ----------------------------------------------------------------------- |
| **Return address**      | The address where the CPU should continue after the function finishes   |
| **Function parameters** | Arguments passed to the function                                        |
| **Local variables**     | Variables declared inside the function                                  |
| **Saved registers**     | Values of registers (like PC, base pointer) that must be restored later |
