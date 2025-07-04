from componentes import Circuito, Resistencia


class CircuitoParalelo(Circuito):
    """Clase para representar un circuito en paralelo"""

    def __init__(self, elementos: list[Circuito | Resistencia], voltaje: float):
        self.elementos = elementos
        self.resistencia = self.calcular_resistencia()
        self.voltaje = voltaje
        self.corriente = self.calcular_corriente()

    def __str__(self) -> str:
        return f"""Resistencia total: {self.resistencia} Ohm
Corriente del circuito: {self.corriente} A
Voltaje total: {self.voltaje} V"""

    def calcular_resistencia(self) -> float:
        """Calcula la resistencia del circuito en ohmnios"""
        resistencia_total = 0
        for elem in self.elementos:
            resistencia_total += 1 / elem.resistencia
        return 1 / resistencia_total

    def calcular_corriente(self) -> float:
        """Calcula la corriente del circuito en amperios"""
        return self.voltaje / self.resistencia

    def calcular_voltaje(self) -> float:
        """Calcula el voltaje del circuito en voltios"""
        return self.voltaje
