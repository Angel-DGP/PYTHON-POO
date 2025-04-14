from laptop import Laptop
import random
class Laptop_Buisness(Laptop):
    def __init__(self, marca, procesador, memoria, al_disco,dur_bat,costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.al_disco = al_disco
        self.dur_bat = dur_bat
    def realizar_diagnostico(self):
        resultado_diagnostico = super().realizar_diagnostico()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Conectividad de red"] = resultado_conectividad
        return resultado_diagnostico
    def verificar_conectividad_red(self):
        elementos = ["DISPONIBILIDAD DE RED","ACCESO A SERVIDORES EMPRESARIALES","LATENCIA DE RED"]
        resultados = {}
        for elemento in elementos:
            if random.choice([True,False]):
                resultados[elemento] = "OK"
            else:
                resultados[elemento] = "Algo ha fallado"
        return resultados