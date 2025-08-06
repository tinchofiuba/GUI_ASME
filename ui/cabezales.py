
class Cabezal:
    def __init__(self):
        self.diametro = 1000
        self.espesor = 3 #en mm
        self.tipo = "Semielíptico 2 : 1"
        self.altura = 250
        self.corr_interna = 0
        self.corr_externa = 0
        self.conformado = "Caliente"
        self.radio_filete = 50
        self.radio_corona = 50
        self.S = 1000
        self.E = 1
        self.Phidro = 0
        self.P_externa = 100 #kPa
        
    def chequeo_condicion_limite(self): #cada norma tiene sus límites esto es solo un warning
        print("aún en desarrollo")
        
    def setear_tipo(self, tipo_cabezal):
        self.tipo = tipo_cabezal
        
    def setear_diametro(self, diametro):
        self.diametro = diametro
        
    def setear_tipo_conformado(self, tipo_conformado):
        self.conformado = tipo_conformado
        
    def adicional_factor_conformado(self):
        if self.conformado == "En caliente":
            return self.espesor * 1.1
        elif self.conformado == "En frío":
            return self.espesor * 0.85
        else:
            raise ValueError("Conformado no reconocido")
    
    def calcular_espesor(self, presion):
        self.presion = presion
        
        if self.tipo == "Semielíptico 2 : 1":
            self.espesor = (self.presion * self.diametro) / (2 * self.S * self.E)
            
        elif self.tipo = "Semiesférico":
            self.espesor = (self.presion * self.diametro) / (4 * self.S * self.E)
            
        elif self.tipo == "Toriesférico":
            self.espesor = (self.presion * self.diametro) / (3 * self.S * self.E)
        else:
            self.espesor = None
            
        return self.espesor


        
