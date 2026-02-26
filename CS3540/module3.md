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

#### Why?
 - It works better with probabilities.
 - It makes optimization convex.

### Decision Boundary
<img height="250" alt="image" src="https://github.com/user-attachments/assets/4e701e4f-97d3-4e46-979e-2b5255130784" />
<img height="250" alt="image" src="https://github.com/user-attachments/assets/3f838218-74de-40ad-bf71-2c55623ab070" />
