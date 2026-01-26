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
