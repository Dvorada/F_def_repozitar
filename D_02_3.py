# Importujeme moduly csv a matplotlib.pyplot
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc


# Otevřeme soubor CSV v režimu čtení
with open("C:\Test\D_02_3.csv", "r") as file:
    # Vytvoříme čtečku CSV, která bude číst data ze souboru
    reader = csv.reader(file, delimiter=";")
    # Přeskočíme první řádek, pokud obsahuje hlavičku
    next(reader)
    # Vytvoříme dva prázdné seznamy pro hodnoty X a Y
    X = []
    Y = []
    # Projdeme všechny řádky v souboru
    for row in reader:
        # Přidáme hodnotu X z prvního sloupce do seznamu X
        X.append(float(row[3]))
        # Přidáme hodnotu Y z druhého sloupce do seznamu Y
        Y.append(float(row[2]))

# Vytvoříme nový obrázek s rozměry 10 x 10 palců
plt.figure(figsize=(10, 5))
# Vytvoříme bodový graf z hodnot X a Y
plt.plot(X,Y, 'y-', label="F/deformace")
# Přidáme titulek grafu
plt.title("Graf Jablko D_02_3")
# Přidáme popisky os
# Převedeme hodnoty na čísla
X = np.array(X)
Y = np.array(Y)

# Vyhladíme data pomocí funkce convolve
window = np.ones(5) / 5  # Velikost okna pro vyhlazování
smoothed_Y = np.convolve(Y, window, mode='same')

# Vytvoříme nový obrázek s rozměry 10 x 5 palců
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Graf funkce
ax1.plot(X, Y, 'y-', label="F/deformace")
ax1.set_xlabel('deformace')
ax1.set_ylabel('F[N]')
ax1.set_title('Graf Jablko D_02_3')
ax1.legend()

# Vypočítáme derivaci pomocí np.diff
dYdX = np.diff(smoothed_Y) / np.diff(X)

# Přidáme první hodnotu derivace jako NaN, aby se zachovala délka polí
dYdX = np.insert(dYdX, 0, np.nan)

# Graf derivace
ax2.plot(X, dYdX)
ax2.set_xlabel('deformace')
ax2.set_ylabel('derivace')
ax2.set_title('Průběh derivace')
ax2.set_ylim(bottom=-220)


# Přidáme titulek grafu
plt.title("Graf Jablko D_02_3")
# Zobrazíme graf
plt.show()
