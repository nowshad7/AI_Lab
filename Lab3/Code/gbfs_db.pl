:- dynamic t_node/2.

t_node(i, nil).
t_node(a, i).
t_node(b, i).
t_node(d, b).
t_node(e, b).
t_node(f, b).
t_node(g, e).

:- dynamic pq/1.

pq([node(g, 0), node(d, 25), node(a, 55)]).

:- dynamic pp/1.

pp([i, b, e, g]).

