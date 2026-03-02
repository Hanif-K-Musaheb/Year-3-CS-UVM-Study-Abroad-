# [Module 7: Unsupervised Learning - K-Means and PCA](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)
## Unsupervised Learning – K-Means
 - Unsupervised Learning
     - No labels
     - We try to discover structure in data
 - Main unsupervised types:
    - Clustering
    - Dimensionality Reduction
    - Association Rules

K-Means belongs to → **Clustering**

### K-means
>K-Means tries to: Partition data into K clusters such that each point belongs to the cluster with the nearest mean.

>**Important: You must choose K manually**

### How it works
##### Steps
1. Choose K
2. Randomly initialize K centroids
3. Assign points
    - Each point goes to the nearest centroid (usually Euclidean distance).
4. Update centroids
<img width="480" height="35" alt="image" src="https://github.com/user-attachments/assets/d06f945c-776a-4f31-8921-25109c3976b0" />
5.Repeat until convergence
     - Centroids stop moving
     - Or assignments stop changing

### Problems with K learns
1. sensitive to intialisation
2. Must choose K (you dont know the correct amount of clusters)
   - Elbow Method
   - Silhouette Score
3. Assumes Spherical Clusters
   - Different densities
   - Non-spherical shapes
   - Different cluster sizes

### K-Means++
>Improves initialization.

##### Instead of random centroids:
1. Pick first centroid randomly.
2. Choose next centroid with probability proportional to distance squared from nearest centroid.

### Accelerated K-Means
Uses triangle inequality to skip unnecessary distance calculations.

### Mini-Batch K-Means
Instead of full dataset each iteration:
Use small random batch

##### Benefits:
 - Much faster
 - Works for huge datasets
 - Slightly less accurate

### Choosing K
#### Elbow Method
 - Plot K vs inertia (Smaller inertia = tighter clusters.)
 - Look for "elbow"
#### Silhouette Score
<img width="122" height="78" alt="image" src="https://github.com/user-attachments/assets/432be50b-d0d8-493e-a1ad-15468e8dc76d" />

##### where:

 - a = mean intra-cluster distance
 - b = mean nearest-cluster distance

---------------

### K-means
### steps
#### k means objective function

#### k means limits
