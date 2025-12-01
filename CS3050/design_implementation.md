# [Characteristics of a design and of the implementation](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3050/CS3050home.md)
### Characteristics of a Design

|Charactaristic|Descript|
|---------------|-------|
|Correctness|(obvious)The design must meet all stated requirements, It should fully and accurately represent the system's intended behavior.|
|Completeness|(obvious)All required components, interfaces, and data structures are specified, No missing functionality.|
|Consistency|(obvious)No conflicting definitions, naming conventions, or interfaces, Interfaces must match across modules.|
|Efficiency|(obvious)Design should allow efficient implementation (performance, memory, etc.).|
|Modularity|(obvious)System divided into clear, independent modules.|
|Maintainability|(obvious)Easy to update, fix, or extend later.|
|Reusability|(obvious)Components can be reused in other systems or contexts.|

### Characteristics of an Implementation
|Charactaristic|Descript|
|--------------|--------|
|Correctness|above|
|Readability|Code should be easy to understand (clear names, consistent formatting).|
|Reliability|Code should run without frequent failures.|
|Efficiency|above|
|Testability|Code must be structured so tests can be created and executed easily.|
|Maintainability|above|
|Robustness|Handles errors and unexpected input safely.|

### Goals of Detailed Design

- **Specify internal logic of modules**--- Algorithms, data structures, control flow.
- **Define interfaces precisely** ---Parameters, return types, inputs/outputs.
- **Ensure high cohesion** ---Each module focuses on one purpose.
- **Ensure low coupling** ---Modules depend on each other as little as possible.
- **Prepare modules for coding** ---Design should be so clear that programmers can directly implement it.
- **Support testability** ---Design should make unit testing straightforward.
- **Support maintainability** ---Structure should be easy to modify later.

### Cohesion
> how well the functions within a single module relate to each other

##### High cohesion (GOOD)
 - Module has one clear responsibility.
 - Functions are strongly related.
 - Example: A "FileParser" module only parses files.

##### Low cohesion (BAD)
 - Module does many unrelated tasks.
 - Hard to maintain or understand.
 - Example: A "Utilities" module doing database access + string formatting + logging.

##### Effects
|Effects of High Cohesion|Effects of Low Cohesion|
|-----|-----|
Easier to maintain|Harder to understand
Easier to test|Error-prone
More reliable and reusable|Difficult to modify without breaking something else
Lower complexity|


### Fan-in and Fan-out
> These measure how modules interact.

##### High fan-in (GOOD)
 - Module is widely reused.
 - Suggests a well-designed, general-purpose module.

##### Low fan-in (NEUTRAL/WEAK)
 - Module is rarely reused.
 - Not necessarily bad unless reuse is expected

### Fan-out
> The number of modules that a given module calls or depends on.

##### High fan-out (BAD)
- Module depends on many others.
- Indicates high coupling.
- Changes in many modules can break it.

##### Low fan-out (GOOD)
 - Module is self-contained.
 - Fewer dependencies → easier to maintain.










