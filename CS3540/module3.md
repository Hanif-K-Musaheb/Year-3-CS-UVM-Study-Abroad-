# [Module 3 -- Logistic Regression](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)
##### TLDR: Logistic regression = linear model + sigmoid → outputs probabilities for classification.
>Despite the name, logistic regression is used for classification, not regression.

>It predicts the probability that something belongs to a class.

1. Computes a linear combination:

<img width="108" height="57" alt="image" src="https://github.com/user-attachments/assets/f16f0c16-9169-42f5-8308-052e53e0108d" />

2. Passes it through a sigmoid function: 

<img width="169" height="80" alt="image" src="https://github.com/user-attachments/assets/b707e7c2-85fe-491f-a005-3f814ebc6942" />

### The Decision Boundary
Even though we use a nonlinear sigmoid, the decision boundary is linear:

<img width="142" height="49" alt="image" src="https://github.com/user-attachments/assets/396281c6-84e5-4f0f-8b9d-4d1374d70806" />

### The Cost Function
It uses log loss (cross-entropy):

<img width="421" height="38" alt="image" src="https://github.com/user-attachments/assets/d0a08d2d-1fa0-4269-a49b-ff507b71f6c5" />

<img height="80" alt="image" src="https://github.com/user-attachments/assets/2ad9a2d2-2e71-4a0e-83f2-108da164427f" />


#### Why?
 - It works better with probabilities.
 - It makes optimization convex.

### Cross entropy
Think of it like this:
 - If the true label is 1
 - And your model predicts 0.99 → good ✅ (small loss)
 - If your model predicts 0.01 → very bad ❌ (huge loss)
   
Cross-entropy heavily punishes being **confident and wrong**.

### Decision Boundary
<img height="250" alt="image" src="https://github.com/user-attachments/assets/4e701e4f-97d3-4e46-979e-2b5255130784" />
<img height="250" alt="image" src="https://github.com/user-attachments/assets/3f838218-74de-40ad-bf71-2c55623ab070" />

------------

## Multi class classification

<img height="200" alt="image" src="https://github.com/user-attachments/assets/cccfa6ea-0354-444d-89d7-277f33419e19" />

-------------

## Decision Tree
### A decision tree is a supervised machine learning model used for:
 - **Classification** (predicting categories)
 - **Regression** (predicting numbers)

### It works like a flowchart:
 - Each **internal node** = a question about a feature
 - Each **branch** = answer to that question
 - Each **leaf node** = final prediction

### The Algorithm That Forms Decision Trees (recursive binary splitting)
#### How it works (step by step):
1. Start with all training data.
2. Try all possible splits on all features.
3. Choose the split that best separates the data.
4. Split the dataset.
5. Repeat recursively until:
   - The data is pure enough, or
   - A stopping rule is met.

### Different Measures Used for Splits
>To decide the “best” split, we measure **impurity**.
Gini Impurity Used by CART.
<img width="219" height="57" alt="image" src="https://github.com/user-attachments/assets/7e17fdb5-ba3e-4018-bfc0-c9611b176129" />

### Entropy
>Entropy measures disorder (from information theory).
<img width="320" height="50" alt="image" src="https://github.com/user-attachments/assets/db89aff2-cfa3-4969-b0f9-d56cfe7a0823" />

### Information Gain
>We choose the split that gives the largest information gain.
<img width="604" height="36" alt="image" src="https://github.com/user-attachments/assets/b6c1ae42-2b30-4e40-a23f-916be3bcfae5" />

### Regularising Decision Trees
Decision trees can overfit easily (they grow very deep and memorize training data).
#### Common Regularization Methods:
 - **Max Depth** - Limit how deep the tree can grow.
 - **Minimum Samples Split** - Minimum number of samples required to split a node.
 - **Minimum Samples Leaf** - Minimum samples allowed in a leaf.
 - **Cost Complexity Pruning** - Grow a big tree first, then prune weak branches.
   




