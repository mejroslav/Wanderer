import os
import time
import random
import webbrowser

BOLD = '\033[1m'
END = '\033[0m'

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
colors = (PURPLE, BLUE, GREEN, YELLOW, RED)


def random_color():
    return random.choice(colors)


class Mesto:
    def __init__(self, poradi, nazev, obyvatele) -> None:
        self.poradi = poradi
        self.nazev = nazev
        self.obyvatele = obyvatele

    def vypis(self):
        c = random_color()
        print(f"Obec {c}{self.nazev}{END} je {c}{self.poradi}. největší{END} v republice bez statutu města. Má {c}{self.obyvatele} obyvatel.{END}")

    def odkaz(self):
        """Po zadání názvu města vrať odkaz na mapy.cz."""
        mesto = self.nazev.lower()
        mesto = mesto.strip()
        mesto_url = f"https://mapy.cz/zakladni?q={mesto}"
        return mesto_url


def vyber_mesto():
    """Vyber náhodné město ze seznamu měst."""
    file = "seznam.txt"
    with open(file, "r+") as r:
        obsah = r.read()
        obsah = obsah.splitlines()

    seznam_mest = []
    for line in obsah:
        radek = line.split("\t")
        mesto = Mesto(radek[0].strip(), radek[1].rstrip(), radek[2].rstrip())
        seznam_mest.append(mesto)

    return random.choice(seznam_mest)


def main():
    print("""          (●>●)          _____     ('~')            ('~')           
 _     _ __/____(ᵔᴥᵔ)  _|     |_  ┐__\|_┌_______   ┐__\|_┌_______   
| | _ | |       |  |  | |  _    ||       |    _ | |       |    _ |  
| || || |   _   |   |_| | | |    |    ___|   | || |    ___|   | ||  
|       |  |_|  |       | |_|    |   |___|   |_||_|   |___|   |_||_ 
|       |       |  _    |        |    ___|    __  |    ___|    __  |
|   _   |   _   | | |   |________|   |___|   |  | |   |___|   |  | |
|__| |__|__| |__|_|  |__| \(●●)/ |_______|___|  |_|_______|___|  |_|

autor: Miroslav Burýšek

Udělej si výlet na nějaké krásné místo v České republice!
""")
    _ = input("Stiskni libovolnou klávesu a vydej se na cestu!")

    nahodne_mesto = vyber_mesto()
    nahodne_mesto.vypis()

    mapa = input("Chceš vyhledat město na mapě? [y/N] ")
    mapa = mapa.lower()

    if (mapa == "y") or (mapa == "yes"):
        try:
            webbrowser.open(nahodne_mesto.odkaz())
        except webbrowser.Error as err:
            print("Něco se pokazilo:")
            print(err)

    exit()


if __name__ == "__main__":
    main()
