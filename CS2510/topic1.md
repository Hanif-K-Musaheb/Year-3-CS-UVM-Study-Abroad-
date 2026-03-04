# [Logic programming, knowledge representation, expert systems](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)
## [**Logic programming**](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/AIlogics.md)
## knowledge representation
Predicate, or first-order logic (FOL), expands on propositional logic. It includes the same connectives and truth values, but adds variables for objects and quantifiers.
### Existential Quantifier
- ∃ -> there exists
    - `(∃𝑥)Φ(𝑥)` There exists some 𝑥 for which the predicate Φ is true.
- 𝑥 ∈ 𝑋 -> x is an element of the set X
    - `(∃𝑥 ∈ 𝑋)Φ(𝑥)` -> there exists x in a X
- Let B(x) mean ”x is blue” --> There exists something, 𝑥, which is blue --> (∃𝑥)𝐵(𝑥)

### Universal quantifier
- ∀ -> for all
- `(∀𝑥)Φ(𝑥)` -> which means for all 𝑥 (in some set or the domain of discourse), the predicate Φ
holds true
 - x an amphibian, M(x) speaks manderin
   - `¬(∃𝑥)𝑀(𝑥)` == `∀(𝑥)¬𝑀 (𝑥)` -> there does not exist an amphibian that speaks manderin



## expert systems
### what is a proof system
A proof system lets us: Derive new facts from existing facts using logical rules.
You start with a Knowledge Base (KB):

 - A set of facts and rules.
 - Then you ask:
 - Does KB imply Q?
 - Is Q necessarily true given KB?
This is written as:
<img width="106" height="37" alt="image" src="https://github.com/user-attachments/assets/acb9b8a6-aca3-4137-ae43-234e607ca27b" />

> This means: n every possible interpretation where KB is true, Q is also true.


### entailment
Entailment (⊨)

This is between:

 - A set of statements (KB)
 - A single statement (Q)
 - KB⊨Q
   
It means:
 - Every model that makes KB true also makes Q true.
