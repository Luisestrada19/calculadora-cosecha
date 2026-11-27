from dataclasses import dataclass
from funcional.calculos import (
    RegistroCosecha,
    calcular_pago_neto,
    calcular_subtotal_registro,
)


@dataclass
class DetallePagoLote:
    lote: str
    subtotal: float
    bono: float
    neto: float
    estado: str


class CalculadoraCosecha:
    def __init__(self, prolog_instance=None):
        self.prolog = prolog_instance

    def evaluar_regla_logica(self, registro: RegistroCosecha) -> tuple[float, str]:
        if self.prolog is not None:
            descanso_atom = "true" if registro.en_descanso else "false"
            consulta = (
                f"aplica_bono({registro.kilos}, {registro.meta_kg}, "
                f"{descanso_atom}, Bono, {registro.bono_fijo}), "
                f"estado_regla({registro.kilos}, {registro.meta_kg}, "
                f"{descanso_atom}, Estado)"
            )
            resultados = list(self.prolog.query(consulta))
            if resultados:
                bono = float(resultados[0]["Bono"])
                estado = str(resultados[0]["Estado"])
                return round(bono, 2), estado

        # Regla equivalente si no se consulta el motor Prolog en tiempo real
        if registro.en_descanso:
            return 0.0, "Restriccion: en descanso"
        if registro.kilos >= registro.meta_kg:
            return round(registro.bono_fijo, 2), "Bono aplicado: meta alcanzada"
        return 0.0, "Sin bono: meta no alcanzada"

    def procesar_registros(self, registros: list[RegistroCosecha]) -> list[DetallePagoLote]:
        detalles: list[DetallePagoLote] = []
        for reg in registros:
            subtotal = calcular_subtotal_registro(reg)
            bono, estado = self.evaluar_regla_logica(reg)
            neto = calcular_pago_neto(subtotal, bono)
            detalles.append(
                DetallePagoLote(
                    lote=reg.lote,
                    subtotal=subtotal,
                    bono=bono,
                    neto=neto,
                    estado=estado,
                )
            )
        return detalles