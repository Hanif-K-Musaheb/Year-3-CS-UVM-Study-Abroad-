# Clocks and Synchronisation
## Clock
>A clock in computer architecture provides the timing signal that coordinates when operations happen inside digital circuits.
#### Key Concepts
 - **Clock Cycle**: One rising (or falling) edge to the next
 - **Clock Frequency**: How many cycles per second (Hz)

## Why Synchronization Is Needed
#### Digital circuits need synchronization because:
- Signals take time to propagate
- Data must arrive at registers at the correct moment
- Prevents errors like data corruption or race conditions

## Synchrous System
>Most processors use synchronous design.
#### Properties:
- All state changes occur on clock edges
- Flip-flops/registers hold data until the next clock tick
- Simplifies design and verification

## Asynchronous Systems
 - Some systems (rare in CPUs) are asynchronous.
#### Characteristics:
 - No global clock
 - Components communicate using handshakes
 - Potentially faster and lower power
 - **MUCH** harder to design and verify

**Clock skew** = when the clock signal arrives at different parts of the CPU at slightly different times.
