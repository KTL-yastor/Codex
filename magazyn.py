class Magazyn:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.lista_produktow = []

    def dodaj_produkt(self, produkt):
        self.lista_produktow.append(produkt)

    def wyswietl_produkty(self):
        for produkt in self.lista_produktow:
            print(produkt)

    def __str__(self):
        return f"Magazyn {self.nazwa} znajduje się w {self.adres}"


class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def __str__(self):
        return f"Produkt {self.nazwa} kosztuje {self.cena} i jest w ilości {self.ilosc}"


magazyn = Magazyn("Magazyn", "ul. Krakowska")

produkt1 = Produkt("Chleb", 2.5, 10)
produkt2 = Produkt("Mleko", 3.5, 20)
produkt3 = Produkt("Jogurt", 1.5, 30)

magazyn.dodaj_produkt(produkt1)
magazyn.dodaj_produkt(produkt2)
magazyn.dodaj_produkt(produkt3)

magazyn.wyswietl_produkty()

print(magazyn)