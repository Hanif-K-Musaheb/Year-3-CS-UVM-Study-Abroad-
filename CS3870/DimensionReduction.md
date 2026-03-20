# [Dimension Reduction](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3870/CS3870.md)
> **Dimensionality Reduction**: simplifying data by reducing the number of variables

> **variance** a measure of how spread out the data points are
## PCA
> PCA is a popular **dimensionality reduction** technique. Its main goal is to take a set of $p$ correlated features and transform them into a smaller set of $q$ uncorrelated features, known as principal components (PCs). This is particularly useful in "large $p$ small $n$" problems, where you have a large number of features but a relatively small sample size.


### finding the first and second principle component and etc
##### First principal component (PC1)
 - It’s the direction of maximum variance
 - Geometrically: the “longest line through the data”

##### Second principal component (PC2)
 - Also maximizes variance
 - BUT must be orthogonal (perpendicular) to PC1

### why it is important to standardize when using PCA
PCA is highly sensitive to the scale of your data. Because PCA aims to maximize variance, a feature with naturally larger numbers (like measuring in millimeters instead of centimeters) will have higher variance and unfairly dominate the first PC. To prevent this, data must always be standardized (rescaled so all variables share a common scale) before running PCA.

### choosing the number of components:
#### Variance Threshold
You can opt to keep enough principal components to explain a specific percentage of the total variance (e.g., 80%). The risk here is that if you set the percentage too high, you might include components that are just modeling specific noise in your sample data.
#### Scree Plot
You can plot the eigenvalues ($\lambda_i$) against the component number. Look for natural breaks or an "elbow" where the steep curve levels out into a straight line. You should retain the components that appear on the steep part of the curve before that flat line begins.
#### 
