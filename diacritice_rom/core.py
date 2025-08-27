import json
import os
from difflib import SequenceMatcher

# Încarcă dicționarul de cuvinte cu diacritice
DICT_PATH = os.path.join(os.path.dirname(__file__), "dict.json")
try:
    with open(DICT_PATH, "r", encoding="utf-8") as f:
        DICT = json.load(f)
except FileNotFoundError:
    DICT = {}


def _similarity(a, b):
    """Calculează similaritatea între două cuvinte (0-1)"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def _validate_correction(original_word, corrected_word, context_words):
    """
    Validează dacă corectarea are sens în context
    """
    # Verifică dacă lungimea nu s-a schimbat dramatic
    length_diff = abs(len(original_word) - len(corrected_word))
    if length_diff > 3:
        return False
    
    # Verifică dacă prima literă este aceeași (pentru a evita confuzii)
    if original_word and corrected_word and original_word[0].lower() != corrected_word[0].lower():
        return False
    
    # Verifică dacă cuvântul corectat nu este prea diferit
    if _similarity(original_word.lower(), corrected_word.lower()) < 0.6:
        return False
    
    return True


def _find_best_match(word, threshold=0.8, context_words=None):
    """
    Găsește cel mai bun match pentru un cuvânt din dicționar
    threshold: similaritatea minimă pentru a considera un match (mărit la 0.8)
    context_words: cuvintele din jur pentru validare
    """
    if word.lower() in DICT:
        return DICT[word.lower()]
    
    best_match = None
    best_score = 0
    
    for dict_word, correct_word in DICT.items():
        # Verifică dacă cuvântul din dicționar este similar
        base_score = _similarity(word.lower(), dict_word)
        
        # Bonus pentru cuvinte care încep la fel (doar dacă sunt suficient de similare)
        if base_score >= 0.7:
            if word.lower().startswith(dict_word[:3]) or dict_word.startswith(word.lower()[:3]):
                base_score += 0.05
            
            # Bonus pentru cuvinte de lungime similară
            length_diff = abs(len(word) - len(dict_word))
            if length_diff <= 1:
                base_score += 0.03
            elif length_diff <= 2:
                base_score += 0.01
        
        # Validează corectarea în context
        if base_score > best_score and base_score >= threshold:
            if _validate_correction(word, correct_word, context_words):
                best_score = base_score
                best_match = correct_word
    
    return best_match


def _preserve_casing(original_word: str, corrected_word: str) -> str:
    """
    Păstrează majusculele inițiale: Romania -> România, ROMANIA -> ROMÂNIA, romania -> românia
    """
    if original_word.isupper():
        return corrected_word.upper()
    if original_word[0].isupper():
        return corrected_word.capitalize()
    return corrected_word


def add_diacritics(text: str, similarity_threshold: float = 0.8) -> str:
    """
    Adaugă diacritice textelor românești folosind un dicționar complet și fuzzy matching îmbunătățit.
    
    Args:
        text: Textul de corectat
        similarity_threshold: Pragul de similaritate pentru detectarea erorilor (0.8 = 80% - mai strict)
    
    Returns:
        Textul corectat cu diacritice
    """
    words = text.split()
    corrected_words = []
    
    for i, word in enumerate(words):
        # Obține contextul (cuvintele din jur)
        context_start = max(0, i - 2)
        context_end = min(len(words), i + 3)
        context_words = words[context_start:context_end]
        
        # Încearcă să găsești un match exact
        if word.lower() in DICT:
            corrected = _preserve_casing(word, DICT[word.lower()])
            corrected_words.append(corrected)
            continue
        
        # Încearcă fuzzy matching pentru cuvinte cu erori (cu validare strictă)
        best_match = _find_best_match(word, similarity_threshold, context_words)
        
        if best_match:
            corrected = _preserve_casing(word, best_match)
            corrected_words.append(corrected)
        else:
            # Dacă nu găsești niciun match, lasă cuvântul neschimbat
            corrected_words.append(word)
    
    return " ".join(corrected_words)


def get_correction_details(text: str, similarity_threshold: float = 0.8) -> dict:
    """
    Returnează detalii despre corectările efectuate.
    
    Returns:
        Dict cu informații despre corectări
    """
    words = text.split()
    corrections = []
    total_corrected = 0
    
    for i, word in enumerate(words):
        # Obține contextul
        context_start = max(0, i - 2)
        context_end = min(len(words), i + 3)
        context_words = words[context_start:context_end]
        
        correction_info = {
            'original': word,
            'corrected': word,
            'type': 'none',
            'confidence': 1.0,
            'context': context_words
        }
        
        # Verifică match exact
        if word.lower() in DICT:
            correction_info['corrected'] = _preserve_casing(word, DICT[word.lower()])
            correction_info['type'] = 'exact'
            correction_info['confidence'] = 1.0
            total_corrected += 1
        else:
            # Verifică fuzzy matching
            best_match = _find_best_match(word, similarity_threshold, context_words)
            if best_match:
                correction_info['corrected'] = _preserve_casing(word, best_match)
                correction_info['type'] = 'fuzzy'
                correction_info['confidence'] = _similarity(word.lower(), best_match.lower())
                total_corrected += 1
        
        corrections.append(correction_info)
    
    return {
        'original_text': text,
        'corrected_text': " ".join([c['corrected'] for c in corrections]),
        'corrections': corrections,
        'total_corrected': total_corrected,
        'total_words': len(words)
    }
