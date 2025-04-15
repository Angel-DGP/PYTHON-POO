class Libro():
    contador_libros = 0
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

        Libro.contador_libros += 1
        pass
    def mostrar_info(self):
        print(f"TITULO: {self.titulo}\nAUTOR: {self.autor}\nCANTIDAD DE PAGINAS: {self.paginas}")
    @staticmethod
    def es_grande(pages):
        return pages>300 
    @classmethod
    def total_libros(cls):
        return cls.contador_libros
