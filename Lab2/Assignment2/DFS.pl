%connected(+Start, +Goal, -Weight)
edge(1,2).
edge(1,4).
edge(2,5).
edge(5,4).
edge(5,3).

connected(X,Y) :- edge(X,Y).
connected(X,Y) :- edge(X,Z), edge(Z,Y).


next_node(Current, Next, Path) :-
    connected(Current, Next, _),
    not(member(Next, Path)).

depth_first(Goal, Goal, _, [Goal],0).
depth_first(Start, Goal, Visited, [Start|Path],L) :-
    next_node(Start, Next_node, Visited),
    edge(Start,Next_node,D),
    depth_first(Next_node, Goal, [Next_node|Visited], Path,L1),
    L is L1+D.
