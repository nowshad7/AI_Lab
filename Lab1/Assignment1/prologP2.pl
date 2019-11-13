parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka'). 
parent('Rashid' , 'Hasib'). 

male('Hasib'). male('Rakib'). male('Sohel'). male('Rashid').
female('Rebeka').

brother(X,Y):-parent(Z,X), parent(Z,Y), male(X), not(X=Y).
sister(X,Y):-parent(Z,X), parent(Z,Y), female(Y), not(X=Y).
/*uncle(X,Y):-parent(Z,Y),brother(Z,X), male(X).
aunt(X,Y):-parent(Z,Y),brother(Z,X), not male(X).


 Procedure to find the grandparent of X */



findBr :-write('person: '), read(Y), write('Brother: '),
		brother(Br,Y), write(Br), tab(5), fail.
findBr.

findSis :-write('person: '), read(X), write('Sister: '),
		sister(X,sis), write(sis).
findSis.
