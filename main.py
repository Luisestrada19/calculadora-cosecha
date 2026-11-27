from funcional.calculos import (
    RegistroCosecha,
    calcular_total_kilos,
    calcular_total_subtotales,
)
from multiparadigma.calculadora import CalculadoraCosecha


def main() -> None:
    prolog = None
    try:
        from pyswip import Prolog  # opcional si tienes SWI-Prolog + pyswip instalado
        prolog = Prolog()
        prolog.consult("logico/reglas_bono.pl")
    except Exception:
        prolog = None

    datos_prueba = [
        RegistroCosecha(lote="Lote A-01", kilos=140.0, tarifa_kg=0.80, meta_kg=120.0, bono_fijo=15.0, en_descanso=False),
        RegistroCosecha(lote="Lote B-03", kilos=95.0,  tarifa_kg=0.80, meta_kg=120.0, bono_fijo=15.0, en_descanso=False),
        RegistroCosecha(lote="Lote C-02", kilos=150.0, tarifa_kg=0.80, meta_kg=120.0, bono_fijo=15.0, en_descanso=True),
    ]

    calc = CalculadoraCosecha(prolog_instance=prolog)
    resultados = calc.procesar_registros(datos_prueba)

    print("=== RESUMEN DIARIO DE COSECHA ===")
    for item in resultados:
        print(
            f"{item.lote} | Subtotal: S/ {item.subtotal:.2f} | "
            f"Bono: S/ {item.bono:.2f} | Neto: S/ {item.neto:.2f} | {item.estado}"
        )

    print(f"Total kilos: {calcular_total_kilos(datos_prueba):.2f} kg")
    print(f"Total subtotales: S/ {calcular_total_subtotales(datos_prueba):.2f}")


if __name__ == "__main__":
    main()