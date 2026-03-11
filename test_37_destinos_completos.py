#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test completo de los 37 destinos nacionales con precios."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.constants import DESTINOS_NACIONALES_DESDE_ARAUCA

def test_37_destinos():
    """Verifica que tenemos exactamente 37 destinos con precios."""
    print("🧪 TESTING: 37 destinos nacionales desde Arauca")
    print("=" * 60)
    
    # Verificar cantidad
    total_destinos = len(DESTINOS_NACIONALES_DESDE_ARAUCA)
    print(f"📊 Total de destinos: {total_destinos}")
    
    if total_destinos != 37:
        print(f"❌ ERROR: Se esperaban 37 destinos, pero hay {total_destinos}")
        return False
    
    print("✅ Cantidad correcta: 37 destinos")
    print("\n📋 Lista completa de destinos con precios:")
    print("-" * 60)
    
    # Mostrar todos los destinos con formato de menú
    for i, destino in enumerate(DESTINOS_NACIONALES_DESDE_ARAUCA, 1):
        precio_formateado = f"${destino['precio']:,}".replace(",", ".")
        print(f"{i:2d}. {destino['nombre']} ({destino['departamento']}) - {precio_formateado}")
    
    # Verificar que todos tienen precio
    sin_precio = [d for d in DESTINOS_NACIONALES_DESDE_ARAUCA if 'precio' not in d or d['precio'] <= 0]
    if sin_precio:
        print(f"\n❌ ERROR: {len(sin_precio)} destinos sin precio válido:")
        for d in sin_precio:
            print(f"   - {d['nombre']}")
        return False
    
    print("\n✅ Todos los destinos tienen precios válidos")
    
    # Mostrar estadísticas de precios
    precios = [d['precio'] for d in DESTINOS_NACIONALES_DESDE_ARAUCA]
    precio_min = min(precios)
    precio_max = max(precios)
    precio_promedio = sum(precios) / len(precios)
    
    print(f"\n📈 Estadísticas de precios:")
    print(f"   💰 Precio mínimo: ${precio_min:,}".replace(",", "."))
    print(f"   💰 Precio máximo: ${precio_max:,}".replace(",", "."))
    print(f"   💰 Precio promedio: ${precio_promedio:,.0f}".replace(",", "."))
    
    # Verificar destinos más caros
    destinos_caros = [d for d in DESTINOS_NACIONALES_DESDE_ARAUCA if d['precio'] >= 380000]
    print(f"\n🏆 Destinos más caros (≥$380.000):")
    for d in sorted(destinos_caros, key=lambda x: x['precio'], reverse=True):
        precio_formateado = f"${d['precio']:,}".replace(",", ".")
        print(f"   - {d['nombre']}: {precio_formateado}")
    
    print("\n🎉 TEST COMPLETADO EXITOSAMENTE")
    print("✅ Los 37 destinos nacionales están configurados correctamente")
    return True

if __name__ == "__main__":
    success = test_37_destinos()
    sys.exit(0 if success else 1)