# [Module 4 -- Training, Testing, and Validation](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)

### Overfitting
 - **Overfitting** happens when a model fits the training data very well but captures noise instead of the underlying pattern, causing poor generalisation to new data.

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
    
