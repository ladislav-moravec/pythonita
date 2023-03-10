from clovek import Clovek

class Pythonista(Clovek):

    IDE = None


    def __init__(self, jmeno, vek, IDE):
        self.jmeno = jmeno
        self.vek = vek
        self.IDE = IDE


    def programuj(self, pocet_radku):
        if self.unava + pocet_radku/10 <= 20:
            self.unava += pocet_radku/10
        else:
            print("Jsem příliš unavený, abych programoval")


