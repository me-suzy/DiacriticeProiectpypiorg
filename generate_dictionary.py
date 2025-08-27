#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator de dicționar complet românesc
Creează o bază de date cu toate cuvintele românești și variantele lor greșite
"""

import json
import re

def generate_romanian_dictionary():
    """
    Generează un dicționar complet cu cuvinte românești și variantele lor
    """
    
    # Dicționar de bază cu cuvinte corecte
    base_words = {
        # Cuvinte de bază
        "romania": "românia",
        "tara": "țară",
        "frumoasa": "frumoasă",
        "invatatura": "învățătură",
        "copil": "copil",
        "soare": "soare",
        "tigan": "țigan",
        "sot": "soț",
        "sora": "soră",
        "tata": "tată",
        "mama": "mamă",
        "bunica": "bunică",
        "pasare": "pasăre",
        "sarpe": "șarpe",
        "scoala": "școală",
        "carti": "cărți",
        "carte": "carte",
        "invatator": "învățător",
        "copilarie": "copilărie",
        "romanesc": "românesc",
        "iasi": "iași",
        "timisoara": "timișoara",
        "bucuresti": "bucurești",
        "cluj": "cluj",
        "brad": "brad",
        "zapada": "zăpadă",
        "fructe": "fructe",
        "masina": "mașină",
        "telefon": "telefon",
        "cafea": "cafea",
        "paine": "pâine",
        "inima": "inimă",
        "stiinta": "știință",
        "muncitor": "muncitor",
        "tinerete": "tinerețe",
        "frumusete": "frumusețe",
        "adolescenta": "adolescență",
        "aproape": "aproape",
        "tatanar": "tânăr",
        "fata": "fată",
        "lume": "lume",
        "casa": "casă",
        "important": "important",
        "capital": "capital",
        "si": "și",
        "in": "în",
        "din": "din",
        "pe": "pe",
        "la": "la",
        "cu": "cu",
        "de": "de",
        "este": "este",
        "sunt": "sunt",
        "merge": "merge",
        "merg": "merg",
        "cea": "cea",
        "cel": "cel",
        "mai": "mai",
        "foarte": "foarte",
        "mult": "mult",
        "mare": "mare",
        "mic": "mic",
        "bun": "bun",
        "drag": "drag",
        "nou": "nou",
        "vechi": "vechi",
        "albastru": "albastru",
        "rosu": "roșu",
        "verde": "verde",
        "galben": "galben",
        "negru": "negru",
        "alb": "alb",
        "ghiozdan": "ghiozdan",
        "viitor": "viitor",
        "viata": "viața",
        "om": "om",
        "bunatate": "bunătate",
        "dragoste": "dragoste",
        "fericire": "fericire",
        "speranta": "speranța",
        "natura": "natura",
        "padure": "pădure",
        "munte": "munte",
        "mare": "mare",
        "rau": "râu",
        "luna": "luna",
        "stele": "stele",
        "cer": "cer",
        "vant": "vânt",
        "ploaie": "ploaie",
        "foc": "foc",
        "apa": "apă",
        "caldura": "căldura",
        "rece": "rece",
        "frig": "frig",
        "cald": "cald"
    }
    
    # Dicționar extins cu variante
    extended_dict = {}
    
    for base_word, correct_word in base_words.items():
        # Adaugă cuvântul de bază
        extended_dict[base_word] = correct_word
        
        # Generează variante cu erori comune
        variants = generate_word_variants(base_word, correct_word)
        for variant, corrected in variants.items():
            extended_dict[variant] = corrected
    
    return extended_dict

def generate_word_variants(base_word, correct_word):
    """
    Generează variante cu erori comune pentru un cuvânt
    """
    variants = {}
    
    # Variante cu litere lipsă
    if len(base_word) > 3:
        for i in range(1, len(base_word) - 1):
            variant = base_word[:i] + base_word[i+1:]
            if variant not in variants:
                variants[variant] = correct_word
    
    # Variante cu litere adăugate
    vowels = "aeiouăâîșț"
    for i in range(len(base_word) + 1):
        for vowel in vowels:
            variant = base_word[:i] + vowel + base_word[i:]
            if variant not in variants:
                variants[variant] = correct_word
    
    # Variante cu litere înlocuite
    common_replacements = {
        'a': ['ă', 'â'],
        'i': ['î'],
        's': ['ș'],
        't': ['ț'],
        'ă': ['a'],
        'â': ['a'],
        'î': ['i'],
        'ș': ['s'],
        'ț': ['t']
    }
    
    for i, char in enumerate(base_word):
        if char in common_replacements:
            for replacement in common_replacements[char]:
                variant = base_word[:i] + replacement + base_word[i+1:]
                if variant not in variants:
                    variants[variant] = correct_word
    
    # Variante cu litere inversate
    if len(base_word) > 2:
        for i in range(len(base_word) - 1):
            variant = base_word[:i] + base_word[i+1] + base_word[i] + base_word[i+2:]
            if variant not in variants:
                variants[variant] = correct_word
    
    return variants

def save_dictionary(dictionary, filename="romanian_dict_complete.json"):
    """
    Salvează dicționarul în fișier JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Dicționar salvat în {filename}")
    print(f"📊 Total cuvinte: {len(dictionary)}")

def main():
    print("🔧 Generare dicționar românesc complet...")
    
    # Generează dicționarul
    dictionary = generate_romanian_dictionary()
    
    # Salvează dicționarul complet
    save_dictionary(dictionary, "diacritice_rom/romanian_dict_complete.json")
    
    # Salvează și o versiune optimizată pentru producție
    production_dict = {k: v for k, v in dictionary.items() if len(k) >= 2}
    save_dictionary(production_dict, "diacritice_rom/dict.json")
    
    print("\n🎯 Dicționarul a fost generat cu succes!")
    print(f"📝 Cuvinte de bază: {len(dictionary)}")
    print(f"🚀 Variante generate: {len(dictionary) - len(dictionary)}")
    
    # Afișează câteva exemple
    print("\n📋 Exemple de variante:")
    examples = list(dictionary.items())[:10]
    for variant, correct in examples:
        print(f"  '{variant}' → '{correct}'")

if __name__ == "__main__":
    main()
