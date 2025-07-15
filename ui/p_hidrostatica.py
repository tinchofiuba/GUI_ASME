
class PresionesHidrostaticas:
    def __init__(self):
        self.alturas = {"envolvente": 1400, "pollera_sup": 400, "pollera_inf": 1550, "cabezal_inf": 1800, "cabezal_sup": 250}
        self.densidad = 1000  
        self.gravedad = 9.82
        self.presiones = {key: self.densidad * self.gravedad * altura for key, altura in self.alturas.items()}
    
    def calcular_presiones(self):
        return {key: self.densidad * self.gravedad * altura for key, altura in self.alturas.items()}

    def setear_alturas(self, caracteristicas_envolvente, alturas):
        if caracteristicas_envolvente['tipo'] == "Cilíndrico":
            if caracteristicas_envolvente['orientacion'] == "Vertical": #alturas es una lista con 5 valores
                self.alturas["envolvente"] = alturas[0]
                self.alturas["pollera_sup"] = alturas[1]
                self.alturas["pollera_inf"] = alturas[2]
                self.alturas["cabezal_inf"] = alturas[3]
                self.alturas["cabezal_sup"] = alturas[4]
                self.calcular_presiones()
            elif caracteristicas_envolvente['orientacion'] == "Horizontal": #alturas tiene un solo valor para todo el equipo
                self.alturas["envolvente"] = alturas
                self.alturas["pollera_sup"] = alturas
                self.alturas["pollera_inf"] = alturas
                self.alturas["cabezal_inf"] = alturas
                self.alturas["cabezal_sup"] = alturas
                self.calcular_presiones()
        elif caracteristicas_envolvente['tipo'] == "Esférico": #alturas es una lista con 1 valor
            self.alturas["envolvente"] = alturas
            self.alturas["pollera_sup"] = alturas
            self.alturas["pollera_inf"] = alturas
            self.alturas["cabezal_inf"] = alturas
            self.alturas["cabezal_sup"] = alturas
            self.calcular_presiones()
        else:
            raise ValueError("Tipo de envolvente no reconocido")
