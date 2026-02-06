# Notes for the 2nd of Febuary
- `_` anonamous value that you can't access in prolog, unlike other languages such as python
### Boolean Satisfiability (unconstrained)
- A boolean is satfiable if there is some combination of inputs that result in **true**.
- SAT is NP-complete and has `O(2^n)` complexity
##### How is prolog fast at this?
- prolog solves this through **constraints**
- which constraints?
  - Horn clause
### Horn Clause
- All prolog is based on Horn clauses _(Alfred Horn 1959)_
- A Horn clause is a disjunction with at most one positive literal
- `∧` conjuntion, `∨`disjunction
### Types of Horn clause
#### Unit clause
 - A unit clause contains a **single** literal, which can be **positive** or **negative**.
 - Unit clauses represent basic **facts** or **fixed** truth values.
 - Example: `𝑃` or `¬P`

#### Negative clause
 - A negative clause is: An **OR** of only **NOT** things
   - No positive variables at all
 - Negative clauses express **constraints** or **inconsistencies**.
 - Example: `¬P∨¬Q` --> `¬(P∧Q)` (De Morgans rule)
 - P and Q are NOT allowed to both be true at the same time.

#### Goal clause
- A goal clause is a negative clause interpreted as a question: “Can this situation occur given my knowledge base?”
- Example: `←P∧Q ≡ (¬P∨¬Q)≡(P∧Q)→false ≡ ¬P∨¬Q` (implication rule `P → Q ≡ ¬P ∨ Q`)



| Clause type     | Positive literals   | Negative literals   | Purpose      |
| --------------- | ------------------- | ------------------- | ------------ |
| Unit clause     | 1 (or 0 if negated) | 0 (or 1 if negated) | Fact         |
| Negative clause | 0                   | ≥1                  | Constraint   |
| Goal clause     | 0                   | ≥1                  | Query / test |



- with horn clauses HORNSAT O(n)  --> Linear time
  - this is why prolog is structured the way it is so that it runs on horn clauses

### AI can of worms
##### What is the most important topics for AI literacy?
> AI is just prediction based on data it has been input

> Programmed to provide answers when don't have any

# Notes for the 4th of Febuary
### Stepwise Funciton
- A stepwise function in Prolog means: A rule that moves the system from one state to the next, one step at a time.
``` prolog
step(X, Y) :-
    Y is X + 1.
```

- **Breadth-First Search** (BFS) is a search method that:
  - explores all states one step away first,
  - then all states two steps away, and so on.
  
### how use last
``` prolog
last(List, LastElement).

%using it in the terminal
?- last([a, b, c, d], X).
X = d.
```


### GPS (General Problem Solver)
 - A problem-solving framework
 - Focuses on states, goals, and operators
 - Explicitly searches through a state space
 - You describe:
   - initial state
   - goal state
   - operators (actions)
     
>**backtracking** is built into the language (similar to human thought)
### Prolog
 - A logic programming language
 - Based on facts and rules
 - Uses logical inference (unification + backtracking)
 - You describe what is true, not how to solve it
   
>**backtracking** is a deliberate search control step
     


# Notes for the 6th of Febuary
> Discussion of Davis , Shrobe , Szolovits

## Knowledge Representation
### 1. **Surgate**
>stands for something else/ stand in representation for the real world
- "All models are wrong. Some models are useful" - George. E. P. Box

  
### 2. **Ontelogical Commitment** 
>study what exist and how it exists
 - blurring and shaping the world for your model
 - **things** - are things you can point to like a laptop
 - **stuff** - are more continous thing like water and butter
 - view of reality not just technical but philosophical


### 3. **Fragmentary Theory of inteligent reasoning**
>facts and rules
 - inferances: possible vs sanctioned
 - frameworks for different models of reasoning

### 4. **medium for pragmatically effiect computation**
- for example horn clauses


### 5. **medium for human expression**
- 




