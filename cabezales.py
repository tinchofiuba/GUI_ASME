
from PyQt5.QtCore import QObject, pyqtSignal

class Cabezales(QObject):
    espedor_calculado = pyqtSignal(float)

    def __init__(self, parent=None):
        super(Cabezales, self).__init__(parent)

    class cabezal_semiesferico:
        def __init__(self, diametro_int, presion, S, E, corr_int, corr_ext):
            self.diametro_int = diametro_int
            self.presion = presion
            self.S = S
            self.E = E
            self.corr_int = corr_int
            self.corr_ext = corr_ext
            
        def calcular_espesor(self):
            return self.presion * self.diametro_int / (2 * self.S * self.E - 0.2 * self.presion)

    class cabezal_semielíptico_2_1:
        def __init__(self, diametro_int, presion, S, E, corr_int, corr_ext):
            self.diametro_int = diametro_int
            self.presion = presion
            self.S = S
            self.E = E
            self.corr_int = corr_int
            self.corr_ext = corr_ext
            
        def calcular_espesor(self):
            return self.presion * (self.diametro_int + 2 * corr_int) / (2 * self.S * self.E - 0.2 * self.presion)