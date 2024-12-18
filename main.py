import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Rejestr książek")
# Wersja po zmianach i dodatkowy komentarz
label_title = tk.Label(root, text="Tytuł książki:", fg="dark green", bg="#FFFF00")
label_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=5)
label_author = tk.Label(root, text="Autor:", fg="blue")
label_author.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_author = tk.Entry(root, width=40)
entry_author.grid(row=1, column=1, padx=10, pady=5)
label_genre = tk.Label(root, text="Gatunek:")
label_genre.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_genre = tk.Entry(root, width=40)
entry_genre.grid(row=2, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Rok wydania:")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
# Przycisk zapisu
button_save = tk.Button(root, text="Zapisz", command=lambda x:x)
button_save.grid(row=4, column=0, columnspan=2, pady=10)
# Uruchomienie pętli głównej
root.mainloop()