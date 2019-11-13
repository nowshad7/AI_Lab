parent('Rashid' , 'Hasib').
parent('Hasib' , 'Rakib').
parent('Hasib' , 'Selina').
parent('Hasib' , 'Jubayer').
parent('Rakib' , 'Sohel').
parent('Selina' , 'Trina').
parent('Jubayer' , 'Shahi').
parent('Jubayer' , 'Barsha').

male('Rashid').
male('Hasib').
male('Rakib').
male('Jubayer').
male('Sohel').
male('Shahi').

brother(X,Y):-parent(Z,X), parent(Z,Y), male(Y), not(X=Y).
sister(X,Y):-parent(Z,X), parent(Z,Y), not(male(Y)), not(X=Y).
uncle(X,Y):-parent(Z,X), parent(W,Z), parent(W,Y), male(Y), not(X=Y).
aunt(X,Y):-parent(Z,X), parent(W,Z), parent(W,Y), not(male(Y)), not(X=Y).


findBr :- write(' Person: '), read(X), write('Brother: '),
		brother(X,Br), write(Br), tab(5), fail.
findBr.

findSs :- write(' Person: '), read(X), write('Sister: '),
		sister(X, Ss), write(Ss), tab(5), fail.
findSs.

findUn :- write(' Person: '), read(X), write('Uncle: '),
		uncle(X, Un), write(Un), tab(5), fail.
findUn.

findAn :- write(' Person: '), read(X), write('Aunt: '),
		aunt(X, An), write(An), tab(5), fail.
findAn.
