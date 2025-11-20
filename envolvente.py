
class Envolvente():
    def __init__(self):
        self.tipo = "Cilíndrico"
        self.orientacion = "Vertical"
        self.altura = 1400
        self.espesor = 3
        self.diametro = 1000

    def calcular_junta_long(self, P, S, E, D):
        """Calcula el espesor de la junta longitudinal."""
        return (P * D) / (2 * S * E)
        
    def calcular_juntas_long_y_circ(self, P, S, E, D):
        #calculo los espesores de las juntas longitudinales y circunferenciales
        if self.tipo == "Cilíndrico":
            t_long = self.calcular_junta_long(P, S, E, D)
            t_circ = self.calcular_junta_long(P, S, E, D)
        
    def calcular_espesor_envolvente(self, P, S, E, D):
        print("Calculando espesor de envolvente")
        # Aquí se implementaría la lógica para calcular el espesor de la envolvente
        # Basado en el tipo de recipiente, orientación, diámetro, etc.
        t_env = self.calcular_juntas_long_y_circ(P, S, E, D)
        
    
        
    