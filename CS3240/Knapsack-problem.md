# [Knapsack problem](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
## [very useful video on it](https://www.youtube.com/watch?v=cJ21moQpofY)
## Core Idea of the knapsack problem
You are given:
 - A set of `n` items
 - Item `i` has:
     - weight `𝑤 𝑖`
     - value `𝑣 𝑖`
 - ​A knapsack with capacity `𝑊`
#### Goal 
Choose a subset of items whose total weight ≤ W and whose total value is maximum.

## OPT Funcition
#### Define
<img width="795" height="24" alt="image" src="https://github.com/user-attachments/assets/e981969d-604a-4776-8327-58be93481e45" />

## Recurrence Relation: Writing OPT in Terms of Other OPT Values
> For each item `𝑖` and capacity `𝑤`, there are two choices:
