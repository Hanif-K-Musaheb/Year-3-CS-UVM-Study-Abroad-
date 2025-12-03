# [Measurements and process models](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3050/CS3050home.md)
## Measurements of Code (Product Metrics)
>These measure characteristics of the software itself—the code, structure, and design.

### Lines of Code (LOC)
>obvious
### Cyclomatic Complexity (McCabe Complexity)
 - **What it measures:**
   - The number of independent paths through the code
   - Essentially: how complicated the logic is
 - **Why it’s useful:**
   - Helps identify code that is difficult to test
   - High complexity ⇒ more bugs likely
   - Highlights functions that should be refactored
### Cohesion
> said in previous topic
### Coupling
### Fan-in / Fan-out
### Code Coverage (from testing)
> **What it measures**: % of code executed by tests

### Defect Density
> **What it measures**: Number of bugs per LOC or per module

## Measurements of Processes (Process Metrics)
>These metrics measure the software development process—how work is done, how fast, how predictable, etc.

### Effort (person-hours / person-days)
### Time / Duration
### Defect Arrival Rate (bugs per week/sprint)
> **What it measures**: Frequency of defects during development or testing
### Velocity (Agile)
> **What it measures**: Amount of work completed in each iteration (e.g., story points)
### Burndown Chart Metrics
> **What they measure**: Remaining work vs time
### Process Compliance (following standards)
>**What it measures**: Whether teams follow required steps (e.g., code reviews, testing, documentation)
### Process Compliance (following standards)
> **What it measures**: Whether teams follow required steps (e.g., code reviews, testing, documentation)
### Defect Removal Efficiency (DRE)
> **What it measures**: % of defects found before release
### Rework Percentage
>**What it measures:** Amount of work done more than once (due to bugs, poor requirements, misunderstandings)

 |**Code Metrics**                       | **Process Metrics**                                   |
| -------------------------------------- | ----------------------------------------------------- |
| Measure the **software product**       | Measure the **way the team develops the product**     |
| Focus on quality of code               | Focus on efficiency & quality of workflow             |
| Examples: LOC, complexity, coupling    | Examples: velocity, defect rate, rework               |
| Help with maintainability, reliability | Help with planning, productivity, process improvement 


