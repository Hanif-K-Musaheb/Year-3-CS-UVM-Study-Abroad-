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
#### Case 1: Do NOT take item i
This gives:

<img width="294" height="26" alt="image" src="https://github.com/user-attachments/assets/637a57db-3b2b-4614-ac67-d9f25f5c975f" />

#### Case 2: Take item 𝑖 (only allowed if 𝑤𝑖≤w)
> If you take item `𝑖` , you gain its value, and you reduce remaining capacity:
<img width="395" height="27" alt="image" src="https://github.com/user-attachments/assets/f931a6c5-c259-46ee-b6f2-052267691713" />

#### Final recurrence
If `𝑤𝑖 ≤ 𝑤`:

<img width="637" height="26" alt="image" src="https://github.com/user-attachments/assets/8b025ccd-2d0e-41d3-9788-c73cfc8d4b96" />

If `𝑤𝑖 > 𝑤`:

<img width="293" height="24" alt="image" src="https://github.com/user-attachments/assets/0b49a241-b21a-42cd-ac9b-ffb07827433d" />​
> These formulas are exactly what your exam expects you to write.

## Base Cases of the OPT Function
> Two base cases must be known:​
<img width="641" height="273" alt="image" src="https://github.com/user-attachments/assets/f2f1a146-d8de-4115-80ff-81997fde7127" />

>These initialize the memoization/DP table.

## How to Solve a Knapsack Problem on an Exam
You must:
1. Write the OPT recurrence correctly.
2. Identify base cases.
3. Construct the DP/memoization table.
4. Fill it row by row, showing which earlier entries were used.
5. The final answer is OPT(n, W) (bottom-right cell).
6. If asked, trace back which items were chosen.

## Summary Cheat-Sheet (ignore if just passing through might delete later bu tmight put on cheat sheet)
<img width="837" height="407" alt="image" src="https://github.com/user-attachments/assets/b850bf97-7b26-4a92-bbe8-b4a51fc6c849" />
