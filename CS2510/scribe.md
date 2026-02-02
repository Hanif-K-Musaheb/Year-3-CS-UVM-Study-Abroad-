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




