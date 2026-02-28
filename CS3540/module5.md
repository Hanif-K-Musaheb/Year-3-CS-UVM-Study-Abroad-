# [Module 5 -- Support Vector Machines](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)


## Support Vector Machines
A Support Vector Machine (SVM) is a supervised machine learning algorithm used mainly for classification (and sometimes regression). Its goal is to find the best possible boundary that separates data points from different classes.
### hard margin classification
>Hard margin SVM is the strict version of SVM classification.

 - It assumes:
   - The data is perfectly linearly separable
   - There is no noise
   - No misclassifications are allowed

<img width="268" height="433" alt="image" src="https://github.com/user-attachments/assets/b04d6472-1c16-46ab-8d26-94decca69ffb" />

  
### Soft margin classification
 - Flexible model, the objective is to find a good balance between keeping the margin as large as possible and limiting the margin violations (i.e., instances that end up in the middle of the margin or even on the wrong side)
 - C is SVM regularization hyperparameter, higher C less violations.
   
<img width="345" height="341" alt="image" src="https://github.com/user-attachments/assets/271111a6-edec-41e1-b69c-2a09d8914518" />

### Nonlinear SVM Classification
 - Linear SVM classifiers are efficient and work surprisingly well in many cases.
 - But many datasets are not even close to being linearly separable.
 - One approach to handling nonlinear datasets is to add more features, such as polynomial features (as we studied before).
<img width="444" height="301" alt="image" src="https://github.com/user-attachments/assets/23384ab8-f14d-48b2-9d60-db033f4e1a8a" />

### Kernel Methods – polynomial
 - Polynomial features can work great with all sorts of Machine Learning algorithms (not just SVMs).
 - Polynomial features cannot deal with very complex datasets, and with a high polynomial degree it creates a huge number of features, making the model too slow, large disk space to save/access data bring many issues
 
 >A **kernel method** is a machine learning technique that lets you solve **non-linear problems using linear algorithms**  by secretly transforming the data into a higher-dimensional space.

#### the core idea
 - Sometimes your data is not linearly separable:
 - You cannot draw a straight line to separate the classes.
 - Instead of giving up, kernel methods do this:
    1. Map the data into a higher-dimensional space
    2. In that new space, the data becomes linearly separable
    3. Apply a linear algorithm there
 - But here’s the trick:
   - You **NEVER** explicitly compute the new high-dimensional features.
   - That trick is called the **kernel trick**.
<img width="360" height="154" alt="image" src="https://github.com/user-attachments/assets/5e1564ff-a192-4c2b-bd79-fdb959edcc76" />

#### What Is a Kernel?
A kernel is just a function that measures similarity between two data points.
##### Linear Kernel
>Just normal dot product.
<img width="197" height="39" alt="image" src="https://github.com/user-attachments/assets/7efe8dec-adbc-409d-8f1a-4be16fabf469" />

##### Polynomial Kernel
>Equivalent to adding polynomial features.
<img width="267" height="36" alt="image" src="https://github.com/user-attachments/assets/841cff88-ed62-462f-93a9-ec060967e6ec" />

##### Gaussian (RBF) Kernel
>Measures distance-based similarity.
<img width="244" height="57" alt="image" src="https://github.com/user-attachments/assets/63e6d74a-e42b-4b48-a0b0-694cf0bdb50a" />

### SVM regression
>SVM supports linear and nonlinear classification, but it also supports linear and nonlinear regression.

- To use SVMs for regression instead of classification, the trick is to reverse the objective: instead of trying to fit the largest possible street between two classes while limiting margin violations, SVM Regression tries to fit as many instances as possible on the street while limiting margin violations (i.e., instances off the street).

- The width of the street is controlled by a hyperparameter, `ε`.



[from slide 29 onwards i am kinda confused](https://brightspace.uvm.edu/d2l/le/content/149373/viewContent/2650562/View)










