% 數學推理知識庫

% 事實
even(2).
even(4).
even(6).
odd(3).
odd(5).

% 規則
even_sum(X, Y, Z) :- even(X), even(Y), Z is X + Y.
odd_sum(X, Y, Z) :- odd(X), odd(Y), Z is X + Y.
mixed_sum(X, Y, Z) :- even(X), odd(Y), Z is X + Y.
