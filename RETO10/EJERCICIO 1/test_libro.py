from libro import Libro
libro1 = Libro("Nadie sabe","Benito",825)
libro2 = Libro("El ultimo baile","Mateo",155)
libro3 = Libro("EL hombre tras el espejo","Michael",465)
libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()
Libro.es_grande(libro1.paginas)
print(f"Los libros creados han sido: {Libro.total_libros()}")