# [Module 6-10](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)
### ensable learning
>Combining multiple models to make one stronger model.
#### Why it works:
 - Reduces variance
 - Reduces overfitting
 - Can reduce bias
 - Makes predictions more stable
#### Hard voting
 - Each model gives a predicted class (not probabilities).
 - The final prediction is the majority vote.
#### Soft voting
 - Each model outputs probability estimates.
 - _Soft voting is usually better because it uses more information._
### Bagging
 - **Bagging**, training models on different random samples of the data.
#### Steps:
 - Randomly sample dataset **with replacement**
 - Train a model on each sample
 - Combine predictions (usually by voting)
#### Why it works:
 - Reduces variance
 - Makes unstable models (like decision trees) more stable

>**Key idea**: Each model sees a slightly different dataset.
### out of bag evaluation
#### When using bagging:
 - Because sampling is done with replacement, some data points are not included in each model’s training set.
 - Those unused samples are called:Out-of-Bag samples
 - We can:
     - Test the model on the data it didn’t see
     - Estimate performance without needing a validation set
 - So:
 - OOB evaluation --> built-in cross-validation for bagging
### Random Forrest
A Random Forest is a specific type of bagging using decision trees.
A Random Forest:
 - Uses bagging
 - Uses decision trees
 - Randomly selects a subset of features at each split
 - Random Forest --> Bagging + Random feature selection + Decision Trees

#### Benefits:
- Very strong baseline model
- Handles high dimensions well
- Resistant to overfitting
- Provides feature importance
  
### Boosting
 - Boosting is different from bagging.
 - Instead of training models independently
 - Models are trained sequentially.
 - Each new model Focuses more on mistakes made by previous models
#### Core idea:
 - Turn many weak learners into one strong learner.
#### Example process:
1. Train weak model
2. Increase weight of misclassified points
3. Train next model focusing on those
4. Combine models (weighted)

#### ada boost
Train weak models sequentially.
Each new model focuses more on the mistakes of the previous ones.
#### Gradient boost

### K-means
#### steps
####k means objective function
#### k means limits


