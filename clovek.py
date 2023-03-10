class Clovek():
    # Třída reprezentuje člověka

    jmeno = None
    vek = None
    unava = 0

    # Konstruktor
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    # Spí danou dobu
    def spi(self, doba):
        self.unava -= doba * 10
        if self.unava < 0:
            self.unava = 0

    # Uběhne danou vzdálenost
    def behej(self, vzdalenost):
        if self.unava + vzdalenost <= 20:
            self.unava += vzdalenost
        else:
            print("Jsem příliš unavený")

    # Textová reprezentace člověka
    def __str__(self):
        return "{0} {1}".format(self.jmeno, self.vek)