from laptopGaming import Laptop_Gaming
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random

class App:
    def __init__(self,root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Clear-Minds\\Analisis de Datos con Python\\POO\\img\laptop-dell-latitude-3420-core-i3-1115g4-4gb-disco-1tb-p-14.webp","C:\\Clear-Minds\\Analisis de Datos con Python\\POO\\img\51svvqLPS4L._AC_SL1000_.jpg"]
        root.title("Ingresar Datos")
        self.setup_ui()
        
    def setup_ui(self):
        ttk.Label(self.root,text="Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)
        
        ttk.Label(self.root,text="Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root,text="Memoria").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root,text="Tarjeta Grafica").grid(row=3,column=0)
        self.tarjeta_grafica = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.tarjeta_grafica).grid(row=3,column=1)

        ttk.Label(self.root,text="Precio").grid(row=4,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.precio).grid(row=4,column=1)
        
        ttk.Button(self.root,text="Agregar",command=self.agregar_laptop).grid(row=5,column=0)
        
        self.mostrat_laptops = tk.Text(self.root,height=10,width=50)
        self.mostrat_laptops.grid(row=6,column=0,columnspan=2)
        
        self.canva = tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=6)
        
        self.mostrar_imagen_aleatorias()
        
    def mostrar_imagen_aleatorias(self):
        image_path = random.choice(self.imagenes)
        imagen = Image.open(image_path)
        imagen_resized = imagen.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(imagen_resized)

        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo

    
    def agregar_laptop(self):
        nueva_laptop = Laptop_Gaming(self.marca.get(),self.procesador.get(),self.memoria.get(),self.tarjeta_grafica.get(),self.precio.get())
        self.laptops.append(nueva_laptop)
        print(self.laptops[0])
        laptop_info = str(self.laptops[0])
        self.mostrat_laptops.insert(tk.END,f"{laptop_info}")
        pass
        
root = tk.Tk()
App = App(root)
root.mainloop()