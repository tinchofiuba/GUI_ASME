import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject


class Model(QObject):

    tipo_recipiente_signal = pyqtSignal()
    tipo_orientacion_signal = pyqtSignal()
    tipo_eficiencia_soldadura_signal = pyqtSignal()
    tipo_cabezal_signal = pyqtSignal()
    

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        
        

