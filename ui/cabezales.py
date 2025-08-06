
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
        
    def setear_corrosion_interna(self, corr_interna):
        self.corr_interna = corr_interna
    
    def setear_corrosion_externa(self, corr_externa):
        self.corr_externa = corr_externa
        
    def setear_radio_filete(self, radio_filete):
        self.radio_filete = radio_filete

    def setear_radio_corona(self, radio_corona):
        self.radio_corona = radio_corona
        
    def setear_tipo(self, tipo_cabezal):
        self.tipo = tipo_cabezal
        
    def setear_diametro(self, diametro):
        self.diametro = diametro
        
    def setear_tipo_conformado(self, tipo_conformado):
        self.conformado = tipo_conformado
        
    def setear_altura_cabezal(self, altura):
        self.altura = altura
        
    def setear_S(self, S):
        self.S = S
        
    def setear_E(self, E):
        self.E = E
        
    def setear_tipo_cabezal(self, tipo_cabezal):
        self.tipo = tipo_cabezal
        
    def setar_tipo_conformado(self, conformado):
        self.conformado = conformado
        
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
            
        elif self.tipo == "Semiesférico":
            self.espesor = (self.presion * self.diametro) / (4 * self.S * self.E)
            
        elif self.tipo == "Toriesférico":
            self.espesor = (self.presion * self.diametro) / (3 * self.S * self.E)
        else:
            self.espesor = None
            
        return self.espesor


        
