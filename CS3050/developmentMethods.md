# [Development Methods](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3050/CS3050home.md)
## Waterfall Method
- This model follow a set of procedures done sequentially and only once
- better for porjects that can be iterative, that must be right on the first try. Like a spaceship software or X ray machine
<img width="1009" height="514" alt="image" src="https://github.com/user-attachments/assets/505944d9-47d1-40ee-b29c-d29241282aa7" />

## Incremental Method
<img width="821" height="407" alt="image" src="https://github.com/user-attachments/assets/b3de3168-d75e-483f-a21f-e3798deb7ecf" />

Advantage | Explanation
|-----|-----|
time to release | the customer does not have to wait for the entire system to be complete before use
feedback | user's feedback from use of early increments helps guide subsequent releases
risk | there is a lower risk of overall project failure (the user will at least get something)
testing | the most important features get the most testing, since they are the first ones that we develop and deploy

Disadvantage 
|-----------|
it can be difficult to map requirements on to separate, staged deliveries
it can be difficult to account for fundamental system components that are needed in all increments
the process is not visible; it can be difficult for project managers to track progress, since the only products of the development are successive versions of the software
system structure tends to degrade as new increments are added


## Component-Based Software Engineering
Basic description: the development team glues together things they already have to produce a system that meets the client's needs

### Advantages and disadvantages:
 - main **advantage** is encapsulation: the team does not have to worry about developing and testing the components that are already available
 - main **disadvantage**: lack of flexibility—the team is constrained by the components they have, and so they have to try to satisfy the requirements within this constraint
### Use Case
It's great for development teams that need to quickly and repeatedly build similar systems
 - **example**: custom scheduling systems for auto-repair businesses or for medical practices

### The need for a design process 
1. **Organization and Control** - A process provides a roadmap that helps teams plan, coordinate, and manage complex work effectively.
2. **Predictability** - Enables better estimation of time, cost, and resource needed for a project
3. **Quality Assurance** - Structured processes include checks and reviews to reduce defects and improve reliability.
4. **Communication** - Establishes a common framework for developers, clients, and stakeholders to understand progress and expectations.
5. **Risk Management** - Helps identify and address potential issues early in development.
6. **Consistency and Repeatability** - Allows teams to replicate success and apply proven practices across multiple projects.
7. **Adaptability** - Processes (especially Agile) allow teams to adapt to changing requirements and environments.
8. **Customer Satisfaction** - A well-managed process ensures that software aligns with user needs, improving satisfaction and trust.

## Phases of software development
 - Finding the rquirements of the software
### 1. **Specification**
#### Activities
 -  Gathering and analyzing user needs and expectations
 -  Defining functional requirements (what the system should do)
 -  Defining non-functional requirements (performance, security, usability, etc.)
 -  Creating a Software Requirements Specification (SRS) document
 -  Reviewing and validating requirements with stakeholders
#### Goals
 - To clearly understand what the software should accomplish
 - To ensure all stakeholders have a shared understanding of system requirements
 - To establish a foundation for design and development
### 2. **Design/Development**
System and Program Design Phase
#### Activities
 - Creating system architecture (overall structure, components, and their interactions)
 - Detailed design of modules, data structures, and algorithms
 - User interface and experience design (UI/UX)
 - Coding / implementation of the design into executable programs
 - Integration of different modules into a working system
#### Goals
 - To define how the system will meet the specified requirements
 - To produce a functional software product that aligns with design specifications
 - To ensure the software is modular, maintainable, and efficient

### 3. Validation
(Testing and verification stage)
#### Activities
 - **Verification**: Checking that the software meets its design specifications 
 - **Validation**: Ensuring the software meets user needs 
 - Conducting unit, integration, system, and acceptance testing
 - Debugging and quality assurance
 - Reviewing performance, usability, and security
#### Goals
 - To ensure the software is correct, reliable, and fit for purpose
 - To identify and fix defects before release
 - To confirm compliance with requirements

### 4. Evolution 
(Maintenance Phase)
#### Activities
 - Monitoring system performance and user feedback after deployment
 - Fixing bugs and security issues
 - Updating and improving functionality based on changing needs
 - Adapting to new hardware, platforms, or business requirements
 - Managing software versions and releases

#### Goals
 - To keep the software useful, secure, and up-to-date over time
 - To adapt to environmental or organizational changes
 - To extend the lifespan and value of the system

### Summary

| **Phase**                | **Main Activities**                             | **Goals**                             | **Waterfall Mapping**          | **Iterative Mapping**                   |
| ------------------------ | ----------------------------------------------- | ------------------------------------- | ------------------------------ | --------------------------------------- |
| **Specification**        | Requirements gathering, analysis, documentation | Define what the system should do      | Done once at the start         | Revisited in every iteration            |
| **Design / Development** | System design, coding, integration              | Build a working, maintainable product | Sequential after specification | Ongoing design + coding in sprints      |
| **Validation**           | Testing, verification, validation               | Ensure correctness and quality        | After all coding is complete   | Continuous testing after each iteration |
| **Evolution**            | Maintenance, updates, bug fixes                 | Keep system relevant and reliable     | Separate post-release phase    | Continuous adaptation and improvement   |

