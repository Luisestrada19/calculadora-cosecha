% aplica_bono(+Kilos, +Meta, +EnDescanso, -MontoBono, -BonoFijo)
aplica_bono(_, _, true, 0.0, _) :- !.
aplica_bono(Kilos, Meta, false, BonoFijo, BonoFijo) :-
    Kilos >= Meta, !.
aplica_bono(_, _, false, 0.0, _).

% estado_regla(+Kilos, +Meta, +EnDescanso, -Estado)
estado_regla(_, _, true, "Restriccion: en descanso") :- !.
estado_regla(Kilos, Meta, false, "Bono aplicado: meta alcanzada") :-
    Kilos >= Meta, !.
estado_regla(_, _, false, "Sin bono: meta no alcanzada").