# [Module 2](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)
### A quick table with most of the symbols and there info:
| Symbol | What It Is | Simple Explanation |
|--------|------------|-------------------|
| θ      | Parameter vector | All the model’s weights grouped into one column vector. It includes the bias term and all feature weights. |
| θ₀     | Bias term | The intercept term. It shifts the prediction up or down. |
| θ₁ … θₙ | Feature weights | The weights that multiply each feature. They control how important each feature is. |
| θᵀ     | Transpose of θ | The same values as θ, but written as a row vector instead of a column vector. |
| X⁽ⁱ⁾   | Feature vector for example i | A column vector containing all features (x₀ to xₙ) for one training example. |
| Y⁽ⁱ⁾   | Label for example i | The true output (target value) for training example i. |
| X      | Feature matrix | All training examples stacked together. Each row is one example’s feature vector. x₀ is always 1 (for the bias term). |
| Y      | Label vector | A column vector containing the true labels for all training examples. |
| Ŷ      | Predicted outputs | The model’s predicted values for all training examples. |

### Linear Regression
- A linear regression models a relationship between variables:
<img width="177" height="44" alt="image" src="https://github.com/user-attachments/assets/9fd518bc-cf3d-45ea-a635-c85b379a3e48" />

- or in vector form:

<img width="99" height="45" alt="image" src="https://github.com/user-attachments/assets/df3e7b76-34d8-40b1-b067-4fa7b41c15c8" />

### Polynomial Regression
>Polynomial regression is still linear regression

>It’s linear in the parameters θ, not in x.

<img width="365" height="67" alt="image" src="https://github.com/user-attachments/assets/136719f8-0e47-4937-9026-c8e8ab3cc7a0" />

##### Cost function / loss function
>This collapses all errors into **one number**.

###### Mean Squared Error:
<img width="263" height="77" alt="image" src="https://github.com/user-attachments/assets/26146e3b-4289-4e8a-aeb0-e0c2c7bd2fe9" />

### Regularization
#### Reduced number of features
>fewer degrees freedom a model has the harder it will to be overfit the data, this can be done easily in polynomaial models by reducing th enumber of polynomial degrees
#### Ridge Regression
<img width="645" height="233" alt="image" src="https://github.com/user-attachments/assets/4689e044-3963-4fa2-97f3-fd9a802cc5a6" />
##### what each part means
 - Sum of Squared Errors (SSE) → measures how wrong the predictions are.
 - λ (lambda) → regularization strength (how much we penalize big weights).
 - ∑𝜃𝑗2 → squared weights (this is called L2 regularization).
 - Important:
   - The bias term 𝜃0 is usually not regularized.
   - Larger weights get penalized more because they are squared.
   - Small λ --> slight shrinking of weights
   - very large λ --> model underfits
   - you want to find the sweet spot inbetween
 - penalty type is L2(squared weights)



#### Difference between feature and data point
| Thing      | Meaning    |
| ---------- | ---------- |
| Data point | One row    |
| Feature    | One column |

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
 
### Lingo
- **Data point / example / sample** = One row of data. `x = 0.4 y = 6.2`
- **m** = number of data points
- **1/m** = average over all data points
- **feature** = One measurable property used to make predictions
- **n** = number of features
- <img width="252" height="148" alt="image" src="https://github.com/user-attachments/assets/b5a69436-17f6-4a73-af83-97998af66c42" />
- **Column of ones / bias / intercept** = The ones column allows the model to shift up/down. __Without it__: Your model must pass through (0,0)
- **y (target / label / output)** = The thing you’re trying to predict
- **θ (theta) — parameters / weights** = θ is what the model learns.
- <img width="849" height="375" alt="image" src="https://github.com/user-attachments/assets/1d94a536-c30f-4adf-a731-4d2750d28d45" />
- **Hypothesis / model / prediction** = <img width="201" height="71" alt="image" src="https://github.com/user-attachments/assets/a0d3796e-9a10-46a9-b744-471623356dcf" />
- **ŷ (y-hat)** if y = real value; then ŷ = model guess
- **Error/Residual** = ŷ-y

