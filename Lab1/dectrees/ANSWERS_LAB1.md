# Lab 1: Decision Trees

### Question 1

Each one of the datasets has properties which makes them hard to learn. Motivate which of the three problems is most difficult for a decision tree algorithm to learn

#### Dataset attributes

| Dataset | True Concept                              |
| ------- | ----------------------------------------- |
| MONK-1  | (a1 = a2) ∨ (a5 = 1)                      |
| MONK-2  | ai = 1 for exactly two i ∈ {1, 2, ..., 6} |
| MONK-3  | (a5 = 1 ∧ a4 = 1) ∨ (a5 ≠ 4 ∧ a2 ≠ 3)     |

| Dataset | # Train | # Test | # Attributes | # Classes |
| ------- | ------- | ------ | ------------ | --------- |
| MONK-1  | 124     | 432    | 6            | 2         |
| MONK-2  | 169     | 432    | 6            | 2         |
| MONK-3  | 122     | 432    | 6            | 2         |

#### Answer

MONK-2 is the hardest dataset for a decision tree to learn because it needs to consider all six attributes at the same time to make the right decision. This makes it more complicated than the other two datasets. In MONK-1, the decision is easier because it uses a disjunction (OR), meaning the tree only needs to check if one of two things is true. In MONK-3, the rule is a combination of conjunctions (AND) and disjunctions (OR), which still makes it easier to handle than MONK-2.

The key difference is that in MONK-2, all conditions must be true for a correct decision (conjunction), which is harder for a decision tree to figure out. In MONK-1 and MONK-3, only some parts of the rule need to be true (disjunction), making them easier to learn.

### Question 2

The file dtree.py defines a function entropy which
calculates the entropy of a dataset. Import this file along with the
monks datasets and use it to calculate the entropy of the training
datasets
...

### Question 3

...

### Question 4

...

### Question 5

...

### Conclusion

...

### References
