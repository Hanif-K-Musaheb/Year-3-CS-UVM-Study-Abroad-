# [AI logics](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)

## Basic symbols

- ¬P : not P  
- P ∧ Q : P and Q  
- P ∨ Q : P or Q (inclusive or)  
- P → Q : if P then Q  
- P ↔ Q : P if and only if Q  



## De Morgan’s Laws 

These tell you how negation interacts with AND / OR:

- ¬(P ∧ Q) ≡ ¬P ∨ ¬Q  
- ¬(P ∨ Q) ≡ ¬P ∧ ¬Q  

“NOT both” = “at least one NOT”  
“NOT either” = “both NOT”



## Implication rules

Implication can always be rewritten:

- P → Q ≡ ¬P ∨ Q  

This is extremely important.



## Contrapositive (very common in proofs)

- P → Q ≡ ¬Q → ¬P  

The contrapositive is logically equivalent.



## What is not equivalent

- Inverse: ¬P → ¬Q ❌  
- Converse: Q → P ❌  

(These are not logically equivalent to P → Q.)


## Double negation

- ¬¬P ≡ P  



## Identity & domination laws

- P ∧ True ≡ P  
- P ∨ False ≡ P  
- P ∧ False ≡ False  
- P ∨ True ≡ True  



## Idempotent laws

- P ∧ P ≡ P  
- P ∨ P ≡ P  



## Commutative laws

- P ∧ Q ≡ Q ∧ P  
- P ∨ Q ≡ Q ∨ P  



## Associative laws

- (P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R)  
- (P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)  



## Distributive laws

- P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)  
- P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)  



## Biconditional

- P ↔ Q ≡ (P → Q) ∧ (Q → P)  

Also: (P ∧ Q) ∨ (¬P ∧ ¬Q)


## Quantifiers

- ∀x : for all x  
- ∃x : there exists an x

## Negation of quantifiers (De Morgan–style)

- ¬(∀x P(x)) ≡ ∃x ¬P(x)  
- ¬(∃x P(x)) ≡ ∀x ¬P(x)  

```
“Not all” = “there exists a counterexample”  
“None exist” = “for all, not”
```

## Satisfiability, validity, and tautology
>well-formed formula (WFF)

 - We call a WFF **satisfiable** if there is at least one interpretation for which it is
true.
 - Conversely, we call a WFF **unsatisfiable** if it is not true for any interpretation.
 - We call a WFF **valid** if it is true for all interpretations.
 - A **tautology** is a WFF whose negation is unsatisfiable. In propositional logic, validity and tautology are equivalent (but this is not so in other logics).












