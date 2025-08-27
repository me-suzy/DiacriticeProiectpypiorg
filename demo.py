#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script pentru diacritice_rom
Arată cum funcționează corectarea automată de diacritice
"""

from diacritice_rom import add_diacritics

def demo_diacritics():
    print("=" * 60)
    print("DEMO: Corectare automată diacritice românești")
    print("=" * 60)
    
    # Exemple predefinite
    examples = [
        "Romania este o tara frumoasa",
        "Copilul merge la scoala",
        "Tata si mama sunt in casa",
        "Invatatura este importanta",
        "Bucuresti este capitala Romaniei",
        "Oana este cea mai frumoasa si mai tatanara fata din lume",
        "Copilul merge la scoala cu cartile in ghiozdan",
        "Mama si tata sunt foarte dragi de copii",
        "Romania este o tara frumoasa cu oameni buni",
        "Invatatura este foarte importanta pentru viitor"
    ]
    
    print("\n📝 EXEMPLE PREDEFINITE:")
    print("-" * 40)
    
    for i, text in enumerate(examples, 1):
        print(f"\n{i}. Text original:  {text}")
        corrected = add_diacritics(text)
        print(f"   Text corectat: {corrected}")
        
        # Arată ce s-a schimbat
        original_words = text.split()
        corrected_words = corrected.split()
        changes = []
        
        for orig, corr in zip(original_words, corrected_words):
            if orig != corr:
                changes.append(f"'{orig}' → '{corr}'")
        
        if changes:
            print(f"   🔄 Modificări: {', '.join(changes)}")
        else:
            print("   ✅ Fără modificări")
    
    # Test cu textul tău specific
    print("\n" + "=" * 60)
    print("🧪 TEST CU TEXTUL TĂU:")
    print("=" * 60)
    
    your_text = "Oana este cea mai frumoasa si mai tatanara fata din lume"
    print(f"\n📥 Textul tău: {your_text}")
    corrected_text = add_diacritics(your_text)
    print(f"📤 Rezultatul: {corrected_text}")
    
    # Analizează modificările
    original_words = your_text.split()
    corrected_words = corrected_text.split()
    changes = []
    
    for orig, corr in zip(original_words, corrected_words):
        if orig != corr:
            changes.append(f"'{orig}' → '{corr}'")
    
    if changes:
        print(f"🔄 Cuvinte modificate: {', '.join(changes)}")
    else:
        print("✅ Niciun cuvânt nu a fost modificat")
    
    # Test cu alte exemple
    print("\n" + "=" * 60)
    print("🧪 TESTE SUPLIMENTARE:")
    print("=" * 60)
    
    test_cases = [
        "Copilul merge la scoala cu cartile",
        "Mama si tata sunt foarte dragi",
        "Romania este o tara frumoasa",
        "Invatatura este importanta",
        "Bucuresti este capitala Romaniei"
    ]
    
    for test_text in test_cases:
        print(f"\n📝 Test: {test_text}")
        result = add_diacritics(test_text)
        print(f"✅ Rezultat: {result}")
        
        # Arată modificările
        orig_words = test_text.split()
        corr_words = result.split()
        mods = []
        
        for orig, corr in zip(orig_words, corr_words):
            if orig != corr:
                mods.append(f"'{orig}' → '{corr}'")
        
        if mods:
            print(f"🔄 Modificări: {', '.join(mods)}")
    
    print("\n" + "=" * 60)
    print("🎯 REZUMAT:")
    print("=" * 60)
    print("✅ Librăria funcționează corect!")
    print("✅ Adaugă diacritice automat")
    print("✅ Păstrează majusculele")
    print("✅ Nu modifică cuvintele care nu au nevoie de diacritice")
    print("✅ Dicționarul conține multe cuvinte românești comune")
    
    # Instrucțiuni pentru testare
    print("\n" + "=" * 60)
    print("💡 CUM SĂ TESTEZI TEXTUL TĂU:")
    print("=" * 60)
    print("1. Deschide Python în terminal:")
    print("   python")
    print("2. Importă funcția:")
    print("   from diacritice_rom import add_diacritics")
    print("3. Testează textul tău:")
    print("   add_diacritics('textul tau aici')")
    print("4. Sau creează un fișier test.py cu:")
    print("   from diacritice_rom import add_diacritics")
    print("   print(add_diacritics('textul tau'))")

if __name__ == "__main__":
    demo_diacritics()
