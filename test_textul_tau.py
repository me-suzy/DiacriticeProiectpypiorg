#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test simplu pentru textul tău
Modifică variabila 'textul_tau' cu textul pe care vrei să-l testezi
"""

from diacritice_rom import add_diacritics

# MODIFICĂ AICI TEXTUL TĂU:
textul_tau = "invattura este frumoasa"

print("=" * 50)
print("TEST TEXTUL TĂU:")
print("=" * 50)

print(f"📥 Textul original: {textul_tau}")
rezultat = add_diacritics(textul_tau)
print(f"📤 Textul corectat: {rezultat}")

# Analizează modificările
cuvinte_originale = textul_tau.split()
cuvinte_corectate = rezultat.split()
modificari = []

for orig, corr in zip(cuvinte_originale, cuvinte_corectate):
    if orig != corr:
        modificari.append(f"'{orig}' → '{corr}'")

if modificari:
    print(f"\n🔄 Cuvinte modificate: {', '.join(modificari)}")
else:
    print("\n✅ Niciun cuvânt nu a fost modificat")

print("\n💡 Pentru a testa alt text, modifică variabila 'textul_tau' în acest fișier!")
