#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo GUI pentru diacritice_rom
Interfață grafică cu pop-up pentru input text
Perfect pentru PyScripter pe Windows
"""

import tkinter as tk
from tkinter import ttk, messagebox
from diacritice_rom import add_diacritics, get_correction_details

class DiacriticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diacritice Rom - Corector Automat")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Stil
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titlu
        title_label = ttk.Label(main_frame, text="🎯 Corector Automat Diacritice Românești", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Buton pentru deschiderea pop-up-ului
        self.popup_button = ttk.Button(main_frame, text="📝 DESCHIDE POP-UP PENTRU TEXT", 
                                      command=self.show_text_popup, style='Accent.TButton')
        self.popup_button.grid(row=1, column=0, columnspan=2, pady=(0, 20), ipadx=20, ipady=10)
        
        # Frame pentru rezultate
        results_frame = ttk.LabelFrame(main_frame, text="📊 Rezultate", padding="15")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Text original
        ttk.Label(results_frame, text="Text Original:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.original_text = tk.Text(results_frame, height=3, width=80, wrap=tk.WORD)
        self.original_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Text corectat
        ttk.Label(results_frame, text="Text Corectat:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.corrected_text = tk.Text(results_frame, height=3, width=80, wrap=tk.WORD)
        self.corrected_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Modificări detaliate
        ttk.Label(results_frame, text="Modificări Detaliate:").grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        self.changes_text = tk.Text(results_frame, height=6, width=80, wrap=tk.WORD)
        self.changes_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Buton pentru testare rapidă
        ttk.Button(main_frame, text="🧪 TESTE RAPIDE", 
                  command=self.show_quick_tests).grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Status
        self.status_label = ttk.Label(main_frame, text="✅ Gata! Apasă butonul pentru a deschide pop-up-ul", 
                                     font=('Arial', 10))
        self.status_label.grid(row=4, column=0, columnspan=2)
        
        # Configurează grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        results_frame.columnconfigure(1, weight=1)
        
        # Stil pentru butonul principal
        style.configure('Accent.TButton', font=('Arial', 12, 'bold'))
        
    def show_text_popup(self):
        """Deschide pop-up-ul pentru input text"""
        popup = tk.Toplevel(self.root)
        popup.title("📝 Introdu Textul Tău")
        popup.geometry("700x500")
        popup.configure(bg='#f0f0f0')
        popup.transient(self.root)
        popup.grab_set()
        
        # Frame principal
        popup_frame = ttk.Frame(popup, padding="20")
        popup_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Instrucțiuni
        ttk.Label(popup_frame, text="Scrie textul pe care vrei să-l corectezi:", 
                 font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Text input
        text_input = tk.Text(popup_frame, height=8, width=70, wrap=tk.WORD, font=('Arial', 11))
        text_input.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        text_input.focus()
        
        # Butoane
        button_frame = ttk.Frame(popup_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        ttk.Button(button_frame, text="✅ Corectează", 
                  command=lambda: self.process_text(text_input.get("1.0", tk.END).strip(), popup)).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(button_frame, text="❌ Anulează", 
                  command=popup.destroy).grid(row=0, column=1)
        
        # Configurează grid
        popup.columnconfigure(0, weight=1)
        popup.rowconfigure(0, weight=1)
        popup_frame.columnconfigure(1, weight=1)
        
        # Centrare pe ecran
        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
        y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
        popup.geometry(f"+{x}+{y}")
        
    def process_text(self, text, popup):
        """Procesează textul introdus"""
        if not text.strip():
            messagebox.showwarning("Atenție", "Te rog să scrii ceva!")
            return
        
        # Obține detalii despre corectări
        details = get_correction_details(text)
        
        # Actualizează rezultatele
        self.original_text.delete("1.0", tk.END)
        self.original_text.insert("1.0", details['original_text'])
        
        self.corrected_text.delete("1.0", tk.END)
        self.corrected_text.insert("1.0", details['corrected_text'])
        
        # Afișează modificările detaliate
        changes_info = []
        for correction in details['corrections']:
            if correction['type'] == 'exact':
                changes_info.append(f"✅ '{correction['original']}' → '{correction['corrected']}' (match exact)")
            elif correction['type'] == 'fuzzy':
                confidence = int(correction['confidence'] * 100)
                changes_info.append(f"🔍 '{correction['original']}' → '{correction['corrected']}' (fuzzy, {confidence}% siguranță)")
            else:
                changes_info.append(f"⏭️  '{correction['original']}' (neschimbat)")
        
        self.changes_text.delete("1.0", tk.END)
        if changes_info:
            self.changes_text.insert("1.0", "\n".join(changes_info))
        else:
            self.changes_text.insert("1.0", "✅ Niciun cuvânt nu a fost modificat")
        
        # Actualizează status
        total_corrected = details['total_corrected']
        total_words = details['total_words']
        self.status_label.config(text=f"✅ Text procesat! {total_corrected}/{total_words} cuvinte corectate.")
        
        # Închide popup-ul
        popup.destroy()
        
    def show_quick_tests(self):
        """Arată teste rapide predefinite"""
        test_window = tk.Toplevel(self.root)
        test_window.title("🧪 Teste Rapide")
        test_window.geometry("800x600")
        test_window.configure(bg='#f0f0f0')
        
        # Frame principal
        test_frame = ttk.Frame(test_window, padding="20")
        test_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(test_frame, text="Teste Rapide Predefinite:", 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Teste cu erori de scriere
        tests = [
            "Romania este o tara frumosa",
            "Copilul merge la scoala cu cartile",
            "Tata si mama sunt in casa",
            "Invatatura este importanta",
            "Bucuresti este capitala Romaniei"
        ]
        
        for i, test_text in enumerate(tests):
            # Text original
            ttk.Label(test_frame, text=f"Test {i+1}:").grid(row=i*3+1, column=0, sticky=tk.W, pady=(10, 5))
            ttk.Label(test_frame, text=test_text, font=('Arial', 10)).grid(row=i*3+1, column=1, sticky=tk.W, padx=(10, 0))
            
            # Rezultat
            result = add_diacritics(test_text)
            ttk.Label(test_frame, text="→").grid(row=i*3+2, column=0, sticky=tk.W)
            ttk.Label(test_frame, text=result, font=('Arial', 10, 'bold')).grid(row=i*3+2, column=1, sticky=tk.W, padx=(10, 0))
            
            # Separator
            if i < len(tests) - 1:
                ttk.Separator(test_frame, orient='horizontal').grid(row=i*3+3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Configurează grid
        test_window.columnconfigure(0, weight=1)
        test_window.rowconfigure(0, weight=1)
        test_frame.columnconfigure(1, weight=1)

def main():
    root = tk.Tk()
    app = DiacriticsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
