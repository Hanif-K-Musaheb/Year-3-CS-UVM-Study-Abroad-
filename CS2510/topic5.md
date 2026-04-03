# [Decision trees, random forest, and ensemble learning](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)
## Decision Trees
### Entropy
>We use entropy to figure out how much information we gain with that being on the decision tree. For example if that question on the decision tree can be used to split the information in half then we have gained a lot of information but if we on split one possibility from it then we have barely gained any information.
### Entropy Calculator
```python
"""
Demonstration of entropy calculation for ID3 classification.

University of Vermont
CS 2990 (2510) Introduction to Artificial Intelligence
Clayton Cafiero <cbcafier@uvm.edu>
"""

from math import log2

EPSILON = 1e-15  # Hack to dodge math domain error on log2(0)


def entropy(bins):
    """Assumes a non-empty list of integers whose sum is not zero. """
    s = 0
    total = sum(bins)
    if total == 0:
        raise ValueError("Sum of bins must not be zero.")
    for count in bins:
        s += -(count / total) * log2(count / total + EPSILON)
    return abs(s)


if __name__ == '__main__':

    counts = []
    print("Enter 'q' to quit when done entering data.")
    while True:
        try:
            n = int(input(f"Enter count for class {len(counts) + 1}: "))
            counts.append(n)
        except ValueError:
            print()
            break

    prob_strs = [f"{x / sum(counts):.3f}" for x in counts]

    print(f"n: {len(counts):,}")
    print(f"Samples: {counts}")
    print(f"Probabilities: [{', '.join(prob_strs)}]")
    print(f"Entropy of {len(counts)} samples: {entropy(counts):.3f}")

```
