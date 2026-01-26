# [Prolog](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)
### Some Prolog syntax
|syntax|meaning|
|----|----|
|`:-`|if|
|`,`|and|
|`;`|or|
|`not`|not|
|`%`|commenting|

### Prolog Rules
 - variables can **only** start with a capital or an underscore
 - **always** put a full stop at the end of lines


### interacting with prolog in terminal
|command|explanation|
|-----|-----|
|`halt.`|	Exits the Prolog terminal and goes back to your regular bash/zsh shell.|
|`make.`	|  Super useful: If you change your .pl file and save it, type make. in the terminal to "refresh" the code without restarting.|
|`[filename].`	|  An alternative way to load a file (e.g., `[autism].`).|
|`;`	|  If Prolog finds one answer and waits, type `;` to ask "Are there any more?"|

#### specific to the script lost.py
|command|result|explanation|
|-----|-----|-----|
|`romance(kate,jack).`|`false.`|asking if there is a romance between kate and jack|
|`enemies(locke,sawyer).`|`true.`|asking if locke and sawyer are enemies|




 ### lost.pl
 >[lost.pl](lost.pl)
 ``` prolog
likes(jack, kate).
likes(jack, hurley).
likes(jack, sayid).
likes(kate, jack).
likes(kate, sawyer).
likes(kate, hurley).
likes(sawyer, kate).
likes(sawyer, hurley).
likes(hurley, jack).
likes(hurley, sawyer).
likes(hurley, sayid).
likes(sayid, jack).
likes(sayid, shannon).
likes(sayid, hurley).
likes(locke, boone).
likes(locke, jack).
likes(boone, locke).
likes(shannon, boone).

loves(shannon, sayid).
loves(sayid, shannon).
loves(boone, shannon).
loves(kate, jack).

dislikes(jack, sawyer).
dislikes(sawyer, jack).
dislikes(sawyer, sayid).
dislikes(sayid, sawyer).
dislikes(shannon, locke).
dislikes(boone, sawyer).

hates(sawyer, locke).
hates(locke, sawyer).
hates(shannon, boone).
hates(boone, locke).

friendship(X, Y) :-
    likes(X, Y),
    likes(Y, X).

romance(X, Y) :-
    loves(X, Y),
    loves(Y, X).

friction(X, Y) :-
    dislikes(X, Y),
    dislikes(Y, X).

enemies(X, Y) :-
    hates(X, Y),
    hates(Y, X).
```
