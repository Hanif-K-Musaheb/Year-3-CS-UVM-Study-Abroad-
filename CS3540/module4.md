# [Module 4 -- Training, Testing, and Validation](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)

### Overfitting
 - **Overfitting** happens when a model fits the training data very well but captures noise instead of the underlying pattern, causing poor generalisation to new data.

<img height="316" alt="image" src="https://github.com/user-attachments/assets/0bc0e603-2814-454d-9564-200c0b2f11f1" />


### Training data
- This is the data the model actually learns from.
- The model adjusts its parameters (weights, coefficients, etc.) to reduce error on this data.
- Think of it as the model’s practice problems.

### Validation data

- This data is not used to update the model’s parameters.
- It’s used to evaluate performance during training.
- Helps you:
  - Tune hyperparameters (learning rate, regularization strength, model size, etc.)
  - Detect overfitting (doing great on training data, badly on unseen data)
 
### Why Accuracy Can Be Misleading
>Imagine:
> - 2000 products
> - Only 10 are defective (0.5%)

>If your model predicts:
> - “Nothing is defective”
> - It gets 99.5% accuracy.

> But it’s useless.
> So accuracy is bad for unbalanced datasets.

### Confusion Matrix
Instead of just **accuracy**, we use:
- **True Positive** (TP)
- **False Positive** (FP)
- **True Negative** (TN)
- **False Negative** (FN)

>From these we compute:

##### Precision
Of everything I predicted as positive, how many were actually positive?

##### Recall
Of everything that was actually positive, how many did I catch?

<img width="519" height="148" alt="image" src="https://github.com/user-attachments/assets/102bd801-0d4b-41d9-b6c6-7cee43974129" />

<img width="418" height="51" alt="image" src="https://github.com/user-attachments/assets/d17f72dd-6861-4cdd-af0d-5a893a115d11" />


### Model Selection Problem
Models have hyperparameters.
##### Examples:
- Regularization strength
- Polynomial degree
- Tree depth

### Receiver Operating Characteristic Curve
<img width="877" height="291" alt="image" src="https://github.com/user-attachments/assets/906fc58a-b6b6-4bf8-aecd-2cfa8e250047" />

 - **Y-axis**: True Positive Rate (TPR)
 - <img width="209" height="82" alt="image" src="https://github.com/user-attachments/assets/2965221c-eae4-42ea-b0b0-4aa70cd8a337" />
 - **X-axis**: False Positive Rate (FPR)
<img width="200" height="77" alt="image" src="https://github.com/user-attachments/assets/93340705-66bd-4d3a-8268-d52dae20d0fc" />
 - A **perfect classifier** goes straight up the left side, then across the top.
 - A **random classifier** gives a diagonal line (like flipping a coin).

#### AUC (Area Under the Curve)
The AUC summarizes performance into one number:
 - **1.0** → Perfect
 - **0.5** → Random guessing

Between 0.5 and 1 → Better than random


### holdout method: 
split dataset into two groups
 - **Training set**: used to train the classifier
 - **Test set**: used to estimate the error rate of the trained classifie

## Cross Validation Evaluation
The limitations of the holdout can be overcome with a
family of resampling methods at the expense of more
computations.
### Repeated random sub-sampling validation

### Bias vs Variance
#### High Bias (Underfitting)
 - Model too simple
 - High training error
 - High test error

#### High Variance (Overfitting)
 - Training error low
 - Test error high
 - Big gap between them
   
### Grid vs Random Search for Model selection
When tuning the hyperparameters of an estimator, Grid Search and Random Search are both popular methods.

### Repeated Random Sub-Sampling Validation
##### What it does
 - Randomly split data into:
   - Training set (e.g., 90%)
   - Validation set (e.g., 10%)
 - Train model
 - Measure validation performance
 - Repeat this many times with different random splits
 - Average the results

### K-Fold Cross Validation (K-Fold CV)
> This is the most common one.

What it does:
 - Split data into K equal parts (folds)
 - For each fold:
   - Use that fold as validation
   - Use the other K−1 folds as training
 - Repeat K times
 - Average performance

### Three-way data splits
>If Both model selection and true error estimates are to be computed
simultaneously, the data needs to be split into three disjoint datasets:
 - Training set: a set of examples used for learning: to fit the parameters of the classifier
 - Validation set: a set of examples used to tune the hyper parameters of a classifier.
 - Test set: a set of examples used only to assess the performance of a fully-trained classifier

<img height="300" alt="image" src="https://github.com/user-attachments/assets/b385edd1-45cc-4557-bd93-1d10bb95e086" />

### Leave-One-Out Cross Validation (LOOCV)
>This is a special case of K-Fold. Used mainly for very small datasets.
<img width="278" height="38" alt="image" src="https://github.com/user-attachments/assets/4f519740-72fa-4501-8148-67021f8cfb9d" />



