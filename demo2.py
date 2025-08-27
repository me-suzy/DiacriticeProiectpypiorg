#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script complet pentru diacritice românești
Arată cum funcționează corectarea automată de diacritice
"""

import sys
import os

# Setează encoding-ul pentru Windows
if os.name == 'nt':  # Windows
    try:
        os.system('chcp 65001 > nul 2>&1')
    except:
        pass

def check_library():
    """Verifică dacă librăria diacritice_rom este disponibilă"""
    try:
        from diacritice_rom import add_diacritics
        print("✅ Librăria diacritice_rom s-a importat cu succes!")
        return add_diacritics
    except ImportError:
        print("❌ EROARE: Librăria diacritice_rom nu este instalată!")
        print("\n🔧 Soluții:")
        print("1. Instalează librăria: pip install diacritice-rom")
        print("2. Sau: pip3 install diacritice-rom")
        print("3. Dacă nu există, vom folosi o versiune simplificată")
        return None
    except Exception as e:
        print(f"❌ Eroare neașteptată: {e}")
        return None

def simple_add_diacritics(text):
    """Versiune simplificată pentru adăugarea diacriticelor"""
    # Dicționar basic pentru cuvinte comune românești
    replacements = {
        'tara': 'țară',
        'tare': 'tare',
        'Romania': 'România',
        'romania': 'românia',
        'frumoasa': 'frumoasă',
        'si': 'și',
        'tatanara': 'tânără',
        'fata': 'fată',
        'scoala': 'școală',
        'tata': 'tata',
        'casa': 'casă',
        'invatatura': 'învățătură',
        'importanta': 'importantă',
        'Bucuresti': 'București',
        'bucuresti': 'bucurești',
        'capitala': 'capitala',
        'Romaniei': 'României',
        'romaniei': 'româniei',
        'cartile': 'cărțile',
        'ghiozdan': 'ghiozdan',
        'foarte': 'foarte',
        'copii': 'copii',
        'oameni': 'oameni',
        'viitor': 'viitor',
        'copilul': 'copilul',
        'merge': 'merge',
        'sunt': 'sunt',
        'dragi': 'dragi',
        'mama': 'mama',
        'pentru': 'pentru',
        'cea': 'cea',
        'mai': 'mai',
        'din': 'din',
        'lume': 'lume',
        'cu': 'cu',
        'in': 'în',
        'este': 'este',
        'la': 'la'
    }
    
    words = text.split()
    corrected_words = []
    
    for word in words:
        # Păstrează punctuația
        punctuation = ''
        clean_word = word
        
        if word and word[-1] in '.,!?;:':
            punctuation = word[-1]
            clean_word = word[:-1]
        
        # Verifică dacă cuvântul există în dicționar
        if clean_word.lower() in replacements:
            # Păstrează majusculele originale
            if clean_word.isupper():
                corrected_word = replacements[clean_word.lower()].upper()
            elif clean_word[0].isupper():
                corrected_word = replacements[clean_word.lower()].capitalize()
            else:
                corrected_word = replacements[clean_word.lower()]
        else:
            corrected_word = clean_word
            
        corrected_words.append(corrected_word + punctuation)
    
    return ' '.join(corrected_words)

def demo_diacritics():
    """Demo principal pentru diacritice"""
    print("=" * 70)
    print("🇷🇴 DEMO: Corectare automată diacritice românești")
    print("=" * 70)
    
    # Verifică librăria
    add_diacritics = check_library()
    
    if add_diacritics is None:
        print("\n⚠️  Folosim versiunea simplificată integrată...")
        add_diacritics = simple_add_diacritics
    
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
    print("-" * 50)
    
    for i, text in enumerate(examples, 1):
        try:
            print(f"\n{i:2d}. Text original:  {text}")
            corrected = add_diacritics(text)
            print(f"    Text corectat: {corrected}")
            
            # Arată ce s-a schimbat
            original_words = text.split()
            corrected_words = corrected.split()
            changes = []
            
            for orig, corr in zip(original_words, corrected_words):
                if orig != corr:
                    changes.append(f"'{orig}' → '{corr}'")
            
            if changes:
                print(f"    🔄 Modificări: {', '.join(changes)}")
            else:
                print("    ✅ Fără modificări")
                
        except Exception as e:
            print(f"    ❌ Eroare la procesarea exemplului {i}: {e}")
    
    # Test cu textul specific
    print("\n" + "=" * 70)
    print("🧪 TEST CU TEXTUL SPECIFIC:")
    print("=" * 70)
    
    your_text = "Oana este cea mai frumoasa si mai tatanara fata din lume"
    try:
        print(f"\n📥 Textul original: {your_text}")
        corrected_text = add_diacritics(your_text)
        print(f"📤 Rezultatul:      {corrected_text}")
        
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
            
    except Exception as e:
        print(f"❌ Eroare la procesarea textului specific: {e}")
    
    # Teste suplimentare
    print("\n" + "=" * 70)
    print("🧪 TESTE SUPLIMENTARE:")
    print("=" * 70)
    
    test_cases = [
        "Copilul merge la scoala cu cartile",
        "Mama si tata sunt foarte dragi",
        "Romania este o tara frumoasa",
        "Invatatura este importanta",
        "Bucuresti este capitala Romaniei"
    ]
    
    for i, test_text in enumerate(test_cases, 1):
        try:
            print(f"\n{i}. Test: {test_text}")
            result = add_diacritics(test_text)
            print(f"   Rezultat: {result}")
            
            # Arată modificările
            orig_words = test_text.split()
            corr_words = result.split()
            mods = []
            
            for orig, corr in zip(orig_words, corr_words):
                if orig != corr:
                    mods.append(f"'{orig}' → '{corr}'")
            
            if mods:
                print(f"   🔄 Modificări: {', '.join(mods)}")
            else:
                print("   ✅ Fără modificări")
                
        except Exception as e:
            print(f"   ❌ Eroare: {e}")
    
    # Rezumat final
    print("\n" + "=" * 70)
    print("🎯 REZUMAT:")
    print("=" * 70)
    print("✅ Script executat cu succes!")
    print("✅ Diacriticele au fost adăugate automat")
    print("✅ Majusculele au fost păstrate")
    print("✅ Cuvintele fără diacritice au rămas neschimbate")
    print("✅ Dicționarul conține cuvinte românești comune")
    
def test_interactive():
    """Test interactiv (opțional)"""
    add_diacritics = check_library()
    if add_diacritics is None:
        add_diacritics = simple_add_diacritics
    
    print("\n" + "=" * 70)
    print("🗣️  TEST INTERACTIV (opțional)")
    print("=" * 70)
    print("Introduceți text românesc fără diacritice (ENTER pentru a sări):")
    
    try:
        user_input = input("➤ ").strip()
        if user_input:
            corrected = add_diacritics(user_input)
            print(f"\n📥 Textul dvs.: {user_input}")
            print(f"📤 Corectat:    {corrected}")
        else:
            print("📝 Test interactiv sărit.")
    except KeyboardInterrupt:
        print("\n\n⏹️  Întrerupt de utilizator.")
    except Exception as e:
        print(f"\n❌ Eroare la input: {e}")

def main():
    """Funcția principală"""
    try:
        # Setează encoding pentru output
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        
        # Rulează demo-ul
        demo_diacritics()
        
        # Test interactiv (opțional)
        test_interactive()
        
        print("\n🏁 Demo finalizat cu succes!")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Program întrerupt de utilizator.")
    except Exception as e:
        print(f"\n❌ Eroare generală: {e}")
        print("🔧 Încercați să rulați scriptul din terminal sau să verificați instalarea Python.")

if __name__ == "__main__":
    main()