# [Logic Gates](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/cs2210/cs2210home.md)
## MOS (metal-oxide semiconductor transistors)
##### [The brightspace page](https://brightspace.uvm.edu/d2l/le/content/134185/viewContent/2426359/View)

### **NMOS** --> N-type metal-oxide semiconductor
 - Here’s how an NMOS transistor works. If there is a source of current connected to terminal S (source), and there’s a low voltage at the gate (G), current will not flow between source and drain (D). However, if sufficient voltage is applied to the gate, current will flow from source to drain.
 - It’s just an electrically-controlled switch. Apply voltage to the gate, and it opens, letting current flow. Turn off the voltage to the gate, and it switches off.

<img width="146" height="110" alt="image" src="https://github.com/user-attachments/assets/c6ffa529-fa1a-474a-8cea-4be5b1b98595" />

### **PMOS** --> P-type metal-oxide semiconductor
Here’s how a PMOS transistor works. If there is a source of current connected to terminal S (source), then if a low voltage is present at the gate (G), current will flow between source and drain (D). However, if sufficient voltage is applied to the gate, current will not flow from source to drain.

Again, it’s just an electrically-controlled switch, but one that’s complementary to the NMOS type. Apply voltage to the gate, and it closes, and no current flows. Turn off the voltage to the gate, and it opens, letting current flow.

<img width="167" height="119" alt="image" src="https://github.com/user-attachments/assets/34f838b4-c248-46e9-84cb-263a0a6c00c6" />




### CMOS (CMOS = complementary metal-oxide semiconductor)
You can see that these two types are complementary. Circuits constructed with these two types are called CMOS circuits (CMOS = complementary metal-oxide semiconductor).

<img width="200" height="290" alt="image" src="https://github.com/user-attachments/assets/ce9cbdfc-00e7-47f0-8b6b-0d3aec75b764" />


You may think of Vdd and the symbol to the right of it as a source for current and a drain or destination for current, respectively. **The black dot indicates a junction where wires are connected. If wires cross and there is no black dot (junction) then the wires are not connected.**

----------------------------

## Multiplexer
A multiplexer (often shortened to MUX) is a digital circuit that selects one input from multiple input signals and forwards it to a single output line.
##### Think of it like an electronic version of a railway switch:
 - You have several "tracks" (inputs).
 - A control signal (called the select line) decides which track is active.
 - The chosen input is sent to the output, while all others are ignored.

#### Key points:
 - A multiplexer has 2ⁿ inputs, n select lines, and 1 output.
 - **Example**: A 4-to-1 MUX has 4 inputs, 2 select lines, and 1 output.
 - It’s essentially a data selector.

#### Commonly used in:
 - Communication systems (choosing between data sources).
 - CPUs (selecting registers or memory locations).
 - Logic circuit optimization.
 - Converts pressed keys (many possible inputs) into binary codes.

-----------------------
## Decoder
<img width="500" height="270" alt="image" src="https://github.com/user-attachments/assets/d9ff975d-35af-4e5c-9d7d-af59ffe5a54f" />

#### Key Points

- **Inputs**: `n` binary signals  
- **Outputs**: `2^n` possible lines  
- For each input combination, only **one output** is active (`1`), while all others remain `0`  
- Often used with **enable inputs** to control whether the decoder is active  

## Encoder
basically the opposite

#### Key Points

- **Inputs**: `2^n` lines (only one active at a time, i.e., one-hot)  
- **Outputs**: `n` binary signals  
- Produces a binary code corresponding to the active input line  
- Often includes a **priority encoder** feature to handle multiple active inputs
  
#### applications

 - Memory Address Decoding
 - Converts binary-coded inputs (like 0001 = 1) to appropriate display signals.
 - Helps in selecting which data line or channel should be active.

Used in RAM and ROM to select a specific memory location.
---------------------
## SR latch
---------------------
## Sequential and Combinational Circuits
### Combinational Circuits
**Definition**:
 - A combinational circuit is a type of digital circuit in which the output depends only on the present inputs — not on any previous inputs or states.
 - No memory is involved.
### Sequential Circuits
**Definition**:
 - A sequential circuit is a digital circuit in which the output depends on both present inputs and past states (previous inputs).

### Summary:
| **Aspect**     | **Combinational Circuit** | **Sequential Circuit**             |
| -------------- | ------------------------- | ---------------------------------- |
| **Depends on** | Present inputs only       | Present inputs + past states       |
| **Memory**     | No                        | Yes                                |
| **Clock**      | Not required              | Usually required                   |
| **Feedback**   | None                      | Has feedback paths                 |
| **Speed**      | Generally faster          | Generally slower (due to clocking) |
| **Examples**   | Adder, MUX, Decoder       | Flip-flop, Counter, Register       |





