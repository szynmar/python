import matplotlib
matplotlib.use('TkAgg')  # Ustawienie backendu przed importem pyplot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definiowanie danych (położenie punktów X i Y)
# Używamy prostych list Pythona
wspolrzedne_x = [1, 2, 3, 4, 5]
wspolrzedne_y = [2, 3, 5, 8, 12]  # Pozycje początkowe

# Stała prędkość dla wszystkich punktów (dx, dy)
# Wszystkie punkty poruszają się z tą samą prędkością
predkosc = [0.08, 0.05]
predkosci = [predkosc.copy() for _ in range(len(wspolrzedne_x))]

# Rozmiar punktów - każdy punkt ma inną wielkość (możesz zmieniać te wartości)
rozmiary_punktow = [100, 150, 200, 250, 300]  # Różne rozmiary dla każdego punktu

# 2. Tworzenie wykresu
wykres, osie = plt.subplots(figsize=(8, 5))
osie.axis('off')  # Wyłącza osie X i Y

# Ustawienie zakresu osi, aby punkty były widoczne przez całą animację
osie.set_xlim(-2, 8)
osie.set_ylim(-2, 20)

# Tworzenie początkowych obiektów (punkty)
punkty = osie.scatter(wspolrzedne_x, wspolrzedne_y, color='red', marker='o', s=rozmiary_punktow)

# Przechowywanie aktualnych pozycji (będą się zmieniać)
aktualne_pozycje = [[wspolrzedne_x[i], wspolrzedne_y[i]] for i in range(len(wspolrzedne_x))]

# 3. Funkcja animacji
# klatka - numer klatki (0, 1, 2, ...)
def animuj(klatka):
    # Aktualizacja pozycji każdego punktu niezależnie
    for i in range(len(aktualne_pozycje)):
        # Dodanie losowej zmiany pozycji (prędkości)
        aktualne_pozycje[i][0] += predkosci[i][0]  # X
        aktualne_pozycje[i][1] += predkosci[i][1]  # Y

        # Odbicie od krawędzi (opcjonalnie, aby punkty nie uciekały z ekranu)
        if aktualne_pozycje[i][0] < -2 or aktualne_pozycje[i][0] > 8:
            predkosci[i][0] *= -1  # Odwróć kierunek X
        if aktualne_pozycje[i][1] < -2 or aktualne_pozycje[i][1] > 20:
            predkosci[i][1] *= -1  # Odwróć kierunek Y

    # Aktualizacja pozycji punktów na wykresie
    punkty.set_offsets(aktualne_pozycje)

    return [punkty]


# 4. Tworzenie animacji
# interval - czas między klatkami w milisekundach (20ms = płynna animacja)
# frames - None oznacza nieskończoną animację
# repeat - czy powtarzać animację
animacja = FuncAnimation(wykres, animuj, frames=None, interval=20, blit=True, repeat=True, cache_frame_data=False)

# 5. Wyświetlenie animacji
# Ta funkcja blokuje program i otwiera okno z wykresem
plt.show()