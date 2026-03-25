# [Module 8 -- Neural Networks](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3540/CS3540.md)
### The perceptron + math
 - A perceptron takes multiple inputs, multiplies them by specific "weights", adds a "bias" term, and then passes that sum through an "activation function" (a non-linear mathematical operation) to generate an output.
 - The formula for this is $y_i = g(\sum_{j=1}^n w_{ij} x_j + b_i)$
 - A single perceptron acts as a linear classifier, meaning it can only solve "linearly separable" problems (data that can be divided by a straight line or flat plane).
 - <img width="136" height="145" alt="image" src="https://github.com/user-attachments/assets/679ca4d3-77a4-4d03-955c-54a2b906782b" />
### Multi Layer Perceptrons(MLPs)
 - Because a single perceptron cannot solve non-linearly separable problems (like the XOR logic gate), we must link them together.An MLP consists of an input layer, one or more "hidden layers," and an output layer.
 - By layering these representations, the network can model highly complex, non-linear functions (like combining AND, OR, and NOT gates to solve the XOR problem).
### Output representation
When using a neural network to classify an image or data point into multiple categories, the network uses "one-hot encoding" (a method where the target class is represented by a 1 and all other classes by 0s).
 - For example, if classifying a dog out of three animals, the output target would be $[0, 0, 1]$.
 - Because raw network outputs are not probabilities, a "Softmax" function is applied to the final layer. This function ensures all output numbers are non-negative and sum exactly to 1, creating a normalized probability distribution.

### Single Perceptrons as Basic Logic Gates
 - **AND Gate**: To create an AND gate, the neuron is given a bias of -15 and a weight of +10 for both inputs ($x_1$ and $x_2$). The mathematical formula is $h_w(x) = g(-15 + 10x_1 + 10x_2)$. Looking at the truth table, the sum is only positive when both inputs are 1 (10 + 10 - 15 = 5), which triggers the function to output a 1.
 - **OR Gate**: For an OR gate, the weights remain +10, but the bias is raised to -5. Because the bias is less negative, if either input is 1, the total sum becomes positive (10 - 5 = 5), resulting in an output of 1.
 - **NOT Gate**: A simple NOT function for a single input is built using a positive bias (+5) and a negative weight (-10). If the input is 0, the sum is 5 (outputting 1); if the input is 1, the sum is -5 (outputting 0).
