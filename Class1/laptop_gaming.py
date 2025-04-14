from laptop import Laptop
class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tar_graf,costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tar_graf = tar_graf
    def realizar_diagnostico(self):
        resultado_diagnostico = super().realizar_diagnostico()
        resultado_juegos = self.rendimiento_juegos()
        resultado_diagnostico["Resultado_juegos"] = resultado_juegos
        return resultado_diagnostico
    def rendimiento_juegos(self):
        juegos = ["FORTNITE","CALL OF DUTY","GTA V"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tar_graf:
                fps = fps_base *3 
            elif "GTX" in self.tar_graf:
                fps = fps_base*2
            else:
                fps = fps_base
            resultados[juego] = f"{fps} FPS"
        return resultados