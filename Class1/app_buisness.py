from laptop_buisness import Laptop_Buisness
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random
class App():
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\User\\Documents\\Work\\M5\\POO\\Class1\\img\\10.png","C:\\Users\\User\\Documents\\Work\\M5\\POO\\Class1\\img\\6.png","C:\\Users\\User\\Documents\\Work\\M5\\POO\\Class1\\img\\7.png","C:\\Users\\User\\Documents\\Work\\M5\\POO\\Class1\\img\\8.png","C:\\Users\\User\\Documents\\Work\\M5\\POO\\Class1\\img\\9.png"]

        root.title("Ingresar Datos")

        self.setup_ui()
        pass
    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)
        
        ttk.Label(self.root, text="Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)
        
        ttk.Label(self.root,text="Memoria RAM").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root,text="Almacenamiento de disco").grid(row=3,column=0)
        self.al_disco = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.al_disco).grid(row=3,column=1)

        ttk.Label(self.root,text="Duración de bateria").grid(row=4,column=0)
        self.dur_bat = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.dur_bat).grid(row=4,column=1)
        
        ttk.Label(self.root,text="Costo").grid(row=5,column=0)
        self.costo = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.costo).grid(row=5,column=1)

        ttk.Button(self.root,text="Guardar", command=self.agregar_laptop).grid(row=6,column=0, columnspan=2)

        self.mostrar_laptops = tk.Text(self.root,height=10, width=50)
        self.mostrar_laptops.grid(row=7,column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200,height=200)
        self.canva.grid(row=0, column=3,rowspan=6)

        pass
    def agregar_laptop(self):
        nueva_laptop = Laptop_Buisness(self.marca.get(),self.procesador.get(),self.memoria.get(),self.al_disco.get(),self.dur_bat.get(),self.costo.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatorias()

        pass
    def mostrar_imagen_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW,image= photo)
        self.canva.image = photo
root = tk.Tk()
app = App(root)
root.mainloop()

