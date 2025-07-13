import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path

# Categorie di file con le relative estensioni
CATEGORIES = {
    "Immagini": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "Video": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
    "Documenti": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"],
    "Archivi": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Eseguibili": [".exe", ".msi", ".bat", ".sh"],
    "Codice": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".php"],
    "Altro": []  # Tutto ciò che non rientra nelle categorie precedenti
}

def organizza_file(cartella_input):
    # Crea le cartelle per ogni categoria se non esistono già
    for categoria in CATEGORIES:
        cartella_categoria = os.path.join(cartella_input, categoria)
        if not os.path.exists(cartella_categoria):
            os.makedirs(cartella_categoria)
    
    # Itera attraverso tutti i file nella cartella di input
    for item in os.listdir(cartella_input):
        item_path = os.path.join(cartella_input, item)
        
        # Salta se è una directory o un file nascosto
        if os.path.isdir(item_path) or item.startswith('.'):
            continue
            
        # Trova la categoria appropriata per il file
        estensione = Path(item).suffix.lower()
        categoria_trovata = "Altro"
        
        for categoria, estensioni in CATEGORIES.items():
            if estensione in estensioni:
                categoria_trovata = categoria
                break
        
        # Sposta il file nella cartella corretta
        cartella_destinazione = os.path.join(cartella_input, categoria_trovata)
        try:
            shutil.move(item_path, cartella_destinazione)
        except Exception as e:
            print(f"Errore durante lo spostamento di {item}: {e}")

def seleziona_cartella():
    cartella = filedialog.askdirectory(title="Seleziona la cartella da organizzare")
    if cartella:
        try:
            organizza_file(cartella)
            messagebox.showinfo("Successo", "File organizzati con successo!")
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore:\n{str(e)}")

# Creazione della GUI
root = Tk()
root.title("Organizzatore File")
root.geometry("400x200")

Label(root, text="Organizzatore File per Categorie", font=("Arial", 14)).pack(pady=10)
Label(root, text="Seleziona una cartella per organizzare i file al suo interno:").pack(pady=10)

Button(root, text="Sfoglia", command=seleziona_cartella, width=15).pack(pady=20)
Button(root, text="Esci", command=root.quit, width=10).pack()

root.mainloop()
