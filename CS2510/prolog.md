# [Prolog](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)
### Some Prolog syntax
|syntax|meaning|
|----|----|
|`:-`|if|
|`,`|and|
|`;`|or|
|`not`,`+\`|not|
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
>**Terminal Tip**: After it shows you one name, press `;` to see the next person, until it says `false` (meaning no more matches).


|command|result|explanation|
|-----|-----|-----|
|`romance(kate,jack).`|`false.`|asking if there is a romance between kate and jack|
|`enemies(locke,sawyer).`|`true.`|asking if locke and sawyer are enemies|
|`friendship(jack,Person).`|` Person = kate ; Person = hurley ; Person = sayid.`| asking who is jack friends with|
|`friction(X,Y).`|`X = jack,Y = sawyer ;X = sawyer,Y = jack ;X = sawyer,Y = sayid ;X = sayid,Y = sawyer ;`|You can ask Prolog to find all pairs of people who fit a certain rule.|
|`likes(jack, Someone), likes(Someone, sawyer).`|`Someone = kate ; Someone = hurley ;`|**Complex Chains** asking who jack likes who also like sawyer|
|`findall(P, survivor(P), List).`| `List = [jack, kate, sawyer, hurley, sayid, sun, jin, charlie, claire …].` |so that you dont have to press `;` every time|


 ### lost.pl
 >[lost.pl](lost.pl)
 ``` prolog
% --- CATEGORIES ---
survivor(jack). survivor(kate). survivor(sawyer). survivor(hurley).
survivor(sayid). survivor(sun). survivor(jin). survivor(charlie).
survivor(claire). survivor(locke). survivor(desmond). survivor(boone).
survivor(shannon).

other(ben). other(juliet). other(richard). other(alex).
other(karl). other(mikhail). other(tom).

outside(penny).

% --- LIKES ---
likes(jack, kate).
likes(jack, juliet).
likes(jack, hurley).
likes(kate, jack).
likes(kate, sawyer).
likes(sawyer, kate).
likes(sawyer, hurley).
likes(hurley, jack).
likes(hurley, sawyer).
likes(hurley, desmond).
likes(sayid, jack).
likes(sayid, sun).
likes(jin, sun).
likes(sun, jin).
likes(sun, sayid).
likes(locke, ben).
likes(locke, boone).
likes(boone, locke).
likes(desmond, charlie).
likes(charlie, desmond).
likes(charlie, hurley).
likes(claire, charlie).
likes(juliet, jack).
likes(juliet, sawyer).
likes(ben, juliet).
likes(richard, ben).
likes(alex, karl).
likes(karl, alex).
likes(mikhail, ben).

% --- LOVES ---
loves(jack, kate).
loves(kate, sawyer).
loves(sawyer, kate).
loves(sayid, shannon).
loves(shannon, sayid).
loves(sun, jin).
loves(jin, sun).
loves(desmond, penny).
loves(penny, desmond).
loves(charlie, claire).
loves(claire, charlie).
loves(juliet, jack).
loves(alex, karl).
loves(karl, alex).

% --- DISLIKES ---
dislikes(jack, sawyer).
dislikes(sawyer, jack).
dislikes(sayid, sawyer).
dislikes(juliet, ben).
dislikes(sawyer, ben).
dislikes(kate, ben).
dislikes(charlie, sawyer).
dislikes(locke, jack).
dislikes(jack, locke).

% --- HATES ---
hates(ben, jack).
hates(jack, ben).
hates(sawyer, tom).
hates(tom, sawyer).
hates(sayid, ben).
hates(mikhail, sayid).
hates(sayid, mikhail).
hates(ben, locke).
hates(locke, ben).

% --- RULES ---

% Basic Relationship Rules
friendship(X, Y) :- likes(X, Y), likes(Y, X).
romance(X, Y) :- loves(X, Y), loves(Y, X).
friction(X, Y) :- dislikes(X, Y), dislikes(Y, X).
enemies(X, Y) :- hates(X, Y), hates(Y, X).

% Love Triangle Rule
love_triangle(Person, Choice1, Choice2) :-
    likes(Person, Choice1),
    likes(Person, Choice2),
    Choice1 \= Choice2,
    (friction(Choice1, Choice2) ; enemies(Choice1, Choice2)).

% The "Secret Agent" (Betrayal Risk) Rule
% Finds characters who like someone, but that person actually hates them.
betrayal_risk(Agent, Target) :-
    likes(Agent, Target),
    hates(Target, Agent).

% Inter-Group Relationship Rule
% Finds an 'Other' who likes a 'Survivor'
bridge_builder(X, Y) :-
    other(X),
    survivor(Y),
    likes(X, Y).
```
