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
calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training
datasets

#### Answer

    Entropy of MONK-1: 1.0
    Entropy of MONK-2: 0.957117428264771
    Entropy of MONK-3: 0.9998061328047111

### Question 3

Explain entropy for a uniform distribution and a
non-uniform distribution, present some example distributions with
high and low entropy

#### Answer

Entropy formula for binary classification problems:

    Entropy(S) = -P0 * log2(P0) - P1 * log2(P1)

In short, entropy is used to measure the uncertainty of a set dataset. The higher the entropy the more uncertain the data is, with lower entropy the data is more certain to predict.

A uniform distribution means that all classes are equally represented in the dataset. This means that the entropy is at its maximum, 1 (when we deal with binary problems). An example of a uniform distribution is a coin toss, since each side has an equal chance of being tossed.

    P0 = 0.5
    P1 = 0.5
    Entropy = -0.5 * log2(0.5) - 0.5 * log2(0.5) = 1

An example of a non-uniform distribution is a dataset where one class is much more common than the others. If you have a box with 90% red balls and 10% blue, the entropy will be lower because there is less uncertainty.

    P0 = 0.9
    P1 = 0.1

    Entropy = -0.9 * log2(0.9) - 0.1 * log2(0.1) = 0.47

### Question 4

Use the function averageGain (defined in dtree.py)
to calculate the expected information gain corresponding to each of
the six attributes. Note that the attributes are represented as in-
stances of the class Attribute (defined in monkdata.py) which you
can access via m.attributes[0], ..., m.attributes[5]. Based on
the results, which attribute should be used for splitting the examples
at the root node

#### Answer

run lab1.py for answer

A5
A6
A2

Maybe add the function to determine the best attribute to split on

### Question 5

For splitting we choose the attribute that maximizes
the information gain, Eq.3. Looking at Eq.3 how does the entropy of
the subsets, Sk, look like when the information gain is maximized?
How can we motivate using the information gain as a heuristic for
picking an attribute for splitting? Think about reduction in entropy
after the split and what the entropy implies

#### Answer

When the information gain is maximized Sk (entropy of the subset) will be minimized.

![Screenshot](images/Screenshot%202024-09-05%20at%2017.09.26.png)

In the image taken from https://www.youtube.com/watch?v=ZVR2Way4nwQ we can see how a decision tree splits data into smaller and smaller subsets. The goal of each split is to reduce the entropy.

Every time we split the data using an attribute, the goal is to reduce uncertainty (entropy) as much as possible. The attribute that provides the highest information gain is the one that most effectively reduces this uncertainty. This is why it is a good heuristic for splitting.

We see in the information gain formula and the image that when information gain is maximized, the entropy is minimized (often reaching zero in some subsets). Information gain directly measures how much uncertainty is reduced after each split and is therefore an effective heuristic. By choosing the attribute that maximizes information gain, we ensure that the decision tree makes the most progress toward classifying the data accurately and efficiently.

### Conclusion

...

### References
