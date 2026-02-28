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
It is very similar to the precision/recall curve, but instead
of plotting precision versus recall, the ROC curve plots
the true positive rate vs False positive rate,

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

### Three-way data splits
>If Both model selection and true error estimates are to be computed
simultaneously, the data needs to be split into three disjoint datasets:
 - Training set: a set of examples used for learning: to fit the parameters of the classifier
 - Validation set: a set of examples used to tune the hyper parameters of a classifier.
 - Test set: a set of examples used only to assess the performance of a fully-trained classifier

  

