# [Markov models and Markov decision processes (MDPs)](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)
## Markov Chains
We use Markov models to model stochastic processes. These are entirely stochastic (based on transi-
tion probabilities) and memoryless (transition probabilities depend only on the current state.
### Markov chains with a stationary distribution
<img width="200" alt="image" src="https://github.com/user-attachments/assets/07318c6c-55bd-432c-b247-c288db353441" />
<img width="300" alt="image" src="https://github.com/user-attachments/assets/7cad5d82-e73c-4d3a-b83b-8df83e6fe555" />
<img width="300"  alt="image" src="https://github.com/user-attachments/assets/e66531b4-986c-49cf-baab-410c61fabd0b" />

### Periodic Markov chains
<img height="150" alt="image" src="https://github.com/user-attachments/assets/ff5f049d-5f50-426c-96f8-a7ade1e39936" />
<img height="150" alt="image" src="https://github.com/user-attachments/assets/5aa2eecd-d11b-4f2d-a091-4dfddd2e43ea" />
<img  height="150" alt="image" src="https://github.com/user-attachments/assets/64ca26c2-3936-461d-9d98-7b54153b4dd7" />

### Absorbing Markov chains
<img height="150" alt="image" src="https://github.com/user-attachments/assets/ae556b37-7f94-4216-bb97-05742d2f6b8b" />
<img height="150" alt="image" src="https://github.com/user-attachments/assets/accf85da-9a4b-4cb2-bba0-ac7dbd1fddd1" />
<img height="150" alt="image" src="https://github.com/user-attachments/assets/f64c9968-d2a9-4c9b-88cf-806261903411" />

## Markov Decision Process (MDP)
An MDP is an extension of a Markov Chain. It provides a mathematical framework for modeling decision-making in situations where outcomes are partly random and partly under the control of a decision-maker (the agent).
#### Core Components:
 - States ($S$): Same as a Markov Chain.
 - Actions ($A$): A set of choices available to the agent in each state.
 - Transition Probabilities ($P$): Unlike a Markov Chain, the probability of moving to the next state depends on both the current state and the action taken by the agent: $P(s' | s, a)$.
 - Rewards ($R$): A numerical value (feedback) given to the agent after performing an action, used to signal success or failure.


