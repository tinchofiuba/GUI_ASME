
class Cabezal:
    def __init__(self):
        self.espesor = 3 #en mm
        self.tipo = "Semielíptico 2 : 1"
        self.altura = 250
        self.corr_interna = 0
        self.corr_externa = 0
        self.conformado = "Caliente"
        self.radio_filete = 50
        self.radio_corona = 50
        
    def chequeo_condicion_limite(self): #cada norma tiene sus límites esto es solo un warning
        print("aún en desarrollo")
        
    def set_corrosion_interna(self, corr_interna):
        self.corr_interna = corr_interna
        self.calcular_espesor_cabezal()
    
    def set_corrosion_externa(self, corr_externa):
        self.corr_externa = corr_externa
        self.calcular_espesor_cabezal()
        
    def set_radio_filete(self, radio_filete):
        self.radio_filete = radio_filete
        self.calcular_espesor_cabezal()
        
    def set_radio_corona(self, radio_corona):
        self.radio_corona = radio_corona
        self.calcular_espesor_cabezal()
        
    def set_tipo(self, tipo_cabezal):
        self.tipo = tipo_cabezal
        self.calcular_espesor_cabezal()
        
    def set_tipo_conformado(self, tipo_conformado):
        self.conformado = tipo_conformado
        self.calcular_espesor_cabezal()
        
    def set_altura_cabezal(self, altura):
        self.altura = altura
        self.calcular_espesor_cabezal()
        
    def set_tipo_cabezal(self, tipo_cabezal):
        self.tipo = tipo_cabezal
        self.calcular_espesor_cabezal()
        
    def set_tipo_conformado(self, conformado):
        self.conformado = conformado
        self.calcular_espesor_cabezal()
        
    def adicional_factor_conformado(self):
        if self.conformado == "En caliente":
            return self.espesor * 1.1
        elif self.conformado == "En frío":
            return self.espesor * 0.85
        else:
            raise ValueError("Conformado no reconocido")
    
    def calcular_espesor(self, P, S, E, D):
        self.chequeo_condicion_limite()
        
        if self.tipo == "Semielíptico 2 : 1":
            self.espesor = (P * D) / (2 * S * E)
        elif self.tipo == "Semiesférico":
            self.espesor = (P * D) / (4 * S * E)

        elif self.tipo == "Toriesférico":
            self.espesor = (P * D) / (3 * S * E)
        else:
            self.espesor = None
            
        return self.espesor


        
