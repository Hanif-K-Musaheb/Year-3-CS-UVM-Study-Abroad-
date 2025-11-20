# [Preventing Errors](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3280/cs3280.md)
> Goal of good design:
 -  Reduce the chance that users can make errors,
 -   Make errors easy to detect,
 -   Make recovery easy, safe, and fast.
### summary
| Error Type   | Subtype                | Definition                                   | Example                       |
| ------------ | ---------------------- | -------------------------------------------- | ----------------------------- |
| **Slips**    | Capture                | Habit overrides intention                    | Driving home instead of store |
|              | Descriptive-Similarity | Right action, wrong similar object           | Clicking wrong file           |
|              | Mode                   | Action behaves differently in different mode | Caps Lock issue               |
|              | Memory-Lapse           | Forgetting an action                         | Forgetting email attachment   |
| **Mistakes** | Rule-based             | Wrong rule applied                           | Wrong formula                 |
|              | Knowledge-based        | Lack of knowledge                            | Misjudging a warning          |
|              | Memory-lapse           | Forgetting the goal                          | Losing track of plan          |

## Causes of Errors
#### Errors happen because of
 - Attention lapses
 - Memory failures
 - Misinterpretations
 - Poor design feedback or signifiers
 - Interruptions or multitasking
 - Wrong mental models
 - Ambiguous controls
 - Poorly designed systems that allow dangerous or meaningless actions
## Slips (Capture, descriptive-similarity, mode, memory-lapse)
> **Slips** – Correct goal, wrong execution


#### Capture Slips
A more frequent, automatic action “captures” the intended action.
##### **Examples:**
 - Typing “gmail.com” when you meant another site because you visit Gmail often
 - Driving home by habit when you meant to stop at the store
 - Clicking “Save” instead of “Save As”
> **Why** Habit overrides intention

#### Descriptive-Similarity Slips
The user performs the correct action on the **wrong object** because items look similar.
##### Examples:
 - Pressing “Delete” on the wrong file because two files have similar names
 - Clicking the wrong window because the icons look alike
 - Grabbing sugar instead of salt due to similar containers
   
#### Mode Slips
The same action does different things **depending on the system’s mode**.
##### Examples:
 - Pressing the arrow key moves the cursor in text mode but moves the object in design mode
 - Caps Lock causing unintended capital letters
 - Camera in “portrait mode” vs “video mode”

> These occur because users forget the system is in a different mode.


#### Memory-Lapse Slips
Forgetting to perform an action or losing track of where you are in a sequence.
##### Examples:
 - Forgetting to attach a file to an email
 - Forgetting a step in a multi-step task
 - Not remembering whether you already pressed “Submit”
> Humans are easily interrupted → memory lapses are inevitable.

## Mistakes (Rule-based, knowledge-based, memory-lapse)
> **Mistakes** – Wrong goal or plan in the first place

## Rule-Based Mistakes
User chooses the wrong rule or guideline to apply.
##### Examples:
 - Selecting the wrong formula in Excel
 - Using an incorrect troubleshooting step
 - Following outdated instructions

## Knowledge-Based Mistakes
> The user lacks the knowledge necessary to make a good decision.
##### Examples:
 - Misinterpreting a medical device interface
 - Guessing how a new system works without proper knowledge
 - Misunderstanding a warning message

## Memory-Lapse Mistakes
> Forgetting the overall goal or losing track of the plan.
> These are deeper than slip memory lapses—they affect goals, not just actions.
##### Examples:
 - Forgetting why you opened an app
 - Starting a process but forgetting the end goal
 - Misdiagnosing a problem because you forgot part of the instructions

## Detecting, reporting and design for errors
#### Design should:
 - Provide clear system status
 - Warn users before dangerous actions
 - Detect invalid input in real-time
 - Validate data immediately (e.g., wrong email format)

#### Reporting Errors
##### When reporting errors:
 - Use plain language, not codes
 - Explain what happened
 - Explain why it happenen
 - Explain how to fix it
 - Highlight the problem area clearly
#### Designing to Prevent Errors
 - Use constraints
 - Provide strong signifiers and mappings
 - Simplify tasks
 - Offer confirmations (only when necessary)
 - Make recovery easy
 - Avoid “modes”

