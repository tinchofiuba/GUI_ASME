import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject


class Model(QObject):

    data_changed = pyqtSignal()

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        
        

