sum(1,_,S,S):-!.

sum(N,I,T,S) :-
   N > 1 ,
        T1 is T+I ,
        N1 is N-1 ,
	sum(N1,I,T1,S1),
	S is S1+T.
