from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class RegistroCosecha:
    lote: str
    kilos: float
    tarifa_kg: float
    meta_kg: float
    bono_fijo: float
    en_descanso: bool = False


def calcular_subtotal_registro(registro: RegistroCosecha) -> float:
    return round(registro.kilos * registro.tarifa_kg, 2)


def calcular_total_kilos(registros: Iterable[RegistroCosecha]) -> float:
    return round(sum(r.kilos for r in registros), 2)


def calcular_total_subtotales(registros: Iterable[RegistroCosecha]) -> float:
    return round(sum(calcular_subtotal_registro(r) for r in registros), 2)


def calcular_pago_neto(subtotal: float, bono: float, descuento: float = 0.0) -> float:
    total = subtotal + bono - descuento
    return round(max(total, 0.0), 2)