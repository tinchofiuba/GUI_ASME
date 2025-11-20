import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject
from cabezales import Cabezal
from envolvente import Envolvente 
from PyQt5.QtWidgets import QMainWindow

class Model(QObject):

    tipo_recipiente_signal = pyqtSignal()
    tipo_orientacion_signal = pyqtSignal()
    tipo_eficiencia_soldadura_signal = pyqtSignal()
    tipo_cabezal_signal = pyqtSignal()
    

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.cab = Cabezal()
        self.env = Envolvente()

    def set_diametro(self, diametro):
        self.env.diametro = diametro

    def calcular_espesor_envolvente(self):
        print("Calculando espesor de envolvente")
        
    def calcular_espesores(self)->float:
        print("Calculando espesores de materiales")
        
    def calcular_espesor_cabezal(self)->float:
        print("Calculando espesor de cabezal")
        
    def set_presion(self, presion):
        self.presion = presion
        self.cab.set_presion(presion)
        print(f"Presión establecida: {self.presion}")
        
    def validar_numerico(self, texto)->bool:
        """Valida si el texto ingresado es un número (entero o decimal)."""
        try:
            float(texto)  
            return True
        except ValueError:
            return False
        
        

