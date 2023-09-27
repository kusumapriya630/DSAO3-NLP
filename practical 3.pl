ha :-
    write('Move disk 1 from '),
    write(A),
    write(' to '),
    write(B),
    nl.
hanoi(N, A, B, C) :-
    N > 1,
    M is N - 1,
    hanoi(M, A, C, B),
    hanoi(1, A, B, _),
    hanoi(M, C, B, A).
