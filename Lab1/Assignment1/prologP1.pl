parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka'). 
parent('Rashid' , 'Hasib'). grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

findGp :- write(' Grandchild: '), read(Z), write('Grandparent: '),
		grandparent(Gp, Z), write(Gp), tab(5), fail.
findGp.
