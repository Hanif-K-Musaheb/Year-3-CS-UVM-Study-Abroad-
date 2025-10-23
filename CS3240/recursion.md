# [Divide and tackle](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)

##### Divide and tackle
- [ ] (come back to) recurrence relations: understanding a recurrence relation; being able to write a
recurrence relation given the description of a divide-and-tackle algorithm
- [ ] unrolling trees: drawing an unrolling tree; showing the total work at each level
- [ ] steps involved in showing a bound for T(n) using an unrolling tree
- [ ] ~~graduate students: be able to set up and complete a proof by induction for a simple
recurrence relation~~
### counting inversions



# Recurrance relation
A recurrence relation expresses the **running time of an algorithm** (or some quantity) in terms of **smaller instances of the same problem**.
> “The total cost = cost of dividing + cost of solving subproblems + cost of combining.”


```T(n)=aT(n/b​)+f(n)```


| Symbol   | Meaning                                                      |
| :------- | :----------------------------------------------------------- |
| ( T(n) ) | time to solve a problem of size ( n )                        |
| ( a )    | number of subproblems                                        |
| ( n/b )  | size of each subproblem                                      |
| ( f(n) ) | cost outside of the recursive calls (divide + combine steps) |
