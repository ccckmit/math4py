% 家族關係知識庫（Prolog 語法）

% 事實
mother(alice, bob).
father(bob, charlie).
father(charlie, david).

% 規則
grandmother(X, Z) :- mother(X, Y), father(Y, Z).
grandfather(X, Z) :- father(X, Y), father(Y, Z).
great_grandmother(X, Z) :- grandmother(X, Y), father(Y, Z).
