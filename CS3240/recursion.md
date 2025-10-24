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


### definitions
 - **base case:** the point at which the recursion stops

##### formula specific to merge
Let’s say:
```T(n)``` = the time it takes to sort a list of size 


###### In Merge Sort:
1. You **divide** the list into 2 halves → takes some time proportional to ```n```
1. You **sort** each half → each half takes ```T(n/2)```
1. You **merge** the two halves → again takes time proportional to ```n```

So we can write:
```T(n)=2T(n/2)+cn```
> the cn is coming from what ever the time to divide + the time to merge is which is unknown 
   
##### General formula meanings

> ```T(n)=aT(n/b​)+f(n)```

| Symbol   | Meaning                                                      |
| :------- | :----------------------------------------------------------- |
| ( T(n) ) | time to solve a problem of size ( n )                        |
| ( a )    | number of subproblems                                        |
| ( n/b )  | size of each subproblem                                      |
| ( f(n) ) | cost outside of the recursive calls (divide + combine steps) |


## Goal
1. **unrolling:** analyzing the first few levels of the algorithm --> then identifying a pattern --> then summing up through all the levels
    - you use this method to find the recurance relation doing it to each level 
3. **intuition:** starting with a guess for the solution --> substituting it in --> proving via induction that it is correct




