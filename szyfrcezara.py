import tkinter as tk
from tkinter import ttk

# Polski alfabet (bez znaków interpunkcyjnych, białych itp.)
alfabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń',
           'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w','x', 'y', 'z', 'ź', 'ż']

# Funkcja szyfrująca tekst
def szyfruj(tekst, klucz):
    wynik = ''
    for znak in tekst.lower():
        if znak in alfabet:
            indeks = alfabet.index(znak)
            nowy_indeks = (indeks + klucz) % len(alfabet)
            wynik += alfabet[nowy_indeks]
    return wynik

# Funkcja deszyfrująca tekst
def deszyfruj(tekst, klucz):
    wynik = ''
    for znak in tekst.lower():
        if znak in alfabet:
            indeks = alfabet.index(znak)
            nowy_indeks = (indeks - klucz) % len(alfabet)
            wynik += alfabet[nowy_indeks]
    return wynik

# Funkcja do obsługi przycisku szyfrującego
def zaszyfruj_tekst():
    tekst = pole_tekstowe.get("1.0", "end-1c")
    klucz = int(klucz_var.get())
    zaszyfrowany_tekst = szyfruj(tekst, klucz)
    wynik_pole.delete("1.0", tk.END)
    wynik_pole.insert(tk.END, zaszyfrowany_tekst)

# Funkcja do obsługi przycisku deszyfrującego
def odszyfruj_tekst():
    tekst = pole_tekstowe.get("1.0", "end-1c")
    klucz = int(klucz_var.get())
    odszyfrowany_tekst = deszyfruj(tekst, klucz)
    wynik_pole.delete("1.0", tk.END)
    wynik_pole.insert(tk.END, odszyfrowany_tekst)

# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Szyfr Cezara - Polski")

# Pole do wprowadzenia tekstu
tk.Label(root, text="Wprowadź tekst:").pack()
pole_tekstowe = tk.Text(root, height=5, width=50)
pole_tekstowe.pack()

# Wybór klucza szyfrującego
klucz_var = tk.StringVar(value="1")
tk.Label(root, text="Wybierz klucz szyfrujący (1-34):").pack()
klucz_wybor = ttk.Combobox(root, textvariable=klucz_var, values=list[str](range(1, 35)), state="readonly")
klucz_wybor.pack()

# Przycisk szyfrujący
szyfruj_button = tk.Button(root, text="Szyfruj", command=zaszyfruj_tekst)
szyfruj_button.pack()

# Przycisk deszyfrujący
deszyfruj_button = tk.Button(root, text="Deszyfruj", command=odszyfruj_tekst)
deszyfruj_button.pack()

# Pole do wyświetlania wyniku
tk.Label(root, text="Wynik:").pack()
wynik_pole = tk.Text(root, height=5, width=50)
wynik_pole.pack()

# Uruchomienie aplikacji
root.mainloop()
