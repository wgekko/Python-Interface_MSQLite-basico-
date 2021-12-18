#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:11:25 2021

@author: walter
"""

from tkinter import *
from tkinter import messagebox
import sqlite3

# -----------------------Funciones-------------------------------

def conexionBBDD():
    miConexion=sqlite3.connect("Usuario")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''CREATE TABLE USUARIO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50),
                                                APELLIDO VARCHAR(50), DIRECCION VARCHAR(60), MAIL VARCHAR(50) UNIQUE,
                                                CLAVE VARCHAR(10), COMENTARIO VARCHAR(300))''')
        
        messagebox.showinfo("Crear BBDD", "Base de datos creada con éxito")
        
    except:
        messagebox.showwarning("¡¡¡ Atención !!!", "la base de datos ya existe")                


def salir():
    valor=messagebox.askquestion("Salir","¿ Desea salir de la aplicación...?")
    if valor=="yes":
        root.destroy()
        

def limpiarCampos():
    
    miId.set("")
    miNombre.set("")   
    miApellido.set("")
    miDireccion.set("")
    miMail.set("")
    miClave.set("")
    textoComentario.delete(1.0,END)
    
    
def crear():
     miConexion=sqlite3.connect("Usuario")
     miCursor=miConexion.cursor()
     # otra opciones de query
     # datos=miNombre.get(),miApellido.get(),miDireccion.get(),miMail.get(), miClave.get(),textoComentario.get("1.0", END) 
     # miCursor.execute("INSERT INTO DATOUSUARIO VALUES (NULL, ?,?,?,?,?,?,?)",(datos))
     
     miCursor.execute("INSERT INTO DATOUSUARIO VALUES ( NULL, '" + miNombre.get() + 
                                                     "','" + miApellido.get() + 
                                                     "','" + miDireccion.get() +
                                                     "','" + miMail.get() +
                                                     "','" + miClave.get() + 
                                                     "','" + textoComentario.get("1.0", END) + "')")   
     
     miConexion.commit()
     
     messagebox.showinfo("Crear", "Registro creado con éxito...")
    
def leer():
     miConexion=sqlite3.connect("Usuario")
     miCursor=miConexion.cursor()
     miCursor.execute("SELECT * FROM DATOUSUARIO WHERE ID=" + miId.get())   
     
     elUsuario=miCursor.fetchall()
     for usuario in elUsuario:
         miId.set(usuario[0])
         miNombre.set(usuario[1])
         miApellido.set(usuario[2])
         miDireccion.set(usuario[3])
         miMail.set(usuario[4])
         miClave.set(usuario[5])
         textoComentario.insert(1.0, usuario[6])        
         
     miConexion.commit()
     
def editar():
     miConexion=sqlite3.connect("Usuario")
     miCursor=miConexion.cursor()
     # otra opciones de query
     # datos=miNombre.get(),miApellido.get(),miDireccion.get(),miMail.get(), miClave.get(),textoComentario.get("1.0", END) 
     # miCursor.execute("UPDATE DATOUSUARIO SET NOMBRE=?, APELLLIDO=?, DIRECCION=?, MAIL=?, CLAVE=?, COMENTARIO=? " + "WHERE ID=" +miId.get(),(datos)) 
     
     miCursor.execute("UPDATE DATOUSUARIO SET NOMBRE='" + miNombre.get() + 
                                                     "', APELLIDO='" + miApellido.get() + 
                                                     "', DIRECCION='" + miDireccion.get() +
                                                     "', MAIL='" + miMail.get() +
                                                     "', CLAVE='" + miClave.get() + 
                                                     "', COMENTARIO='" + textoComentario.get("1.0", END) +
                                                     "' WHERE ID=" + miId.get())   
     
     miConexion.commit()
     
     messagebox.showinfo("Editar", "Registro se ha actualizado con  éxito...")
     
     
def borrar():
     miConexion=sqlite3.connect("Usuario")
     miCursor=miConexion.cursor()
     miCursor.execute("DELETE FROM DATOUSUARIO WHERE ID=" + miId.get())   
     
     miConexion.commit()
     
     messagebox.showinfo("Borrar", "Registro se ha borrado con  éxito...")
     

def licencia():

    messagebox.showinfo("Licencia de Walter Gómez", "A modo de desarrollo de un ejercicio en Python con BBDD,"
                                                          "\n\n"   
                                                         " usando MSQLite"
                                                         "\n\n"                                                         
                                                         " se busca practica en el desarrollo "
                                                          "\n\n"
                                                         "de herramientas de lenguaje Python.")
    
def proyecto():

    messagebox.showinfo("Proyecto CRUD en Python ", "Gestor de Usuarios , es un pequeño proyecto que busca utilizar,"
                                                         "\n\n"                          
                                                         " las herramientas clasicas de crear, leer, actualizar, borrar, "
                                                         "\n\n"   
                                                         " la base de datos usadas es MSQLite, apta para este caso para no  "
                                                         "\n\n"
                                                         " consumir tantos recursos y a modo de practivca de adminitración"
                                                         "\n\n"    
                                                         " de archivos y registros.")
                                                   





#----------------------- fin de funciones -------------------------------

root=Tk()

# --- desarrollo de la barra de menu -----------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=400, height=400)

ArchivoMenu=Menu(barraMenu, tearoff=0)
ArchivoMenu.add_command(label="crear BBDD", command=conexionBBDD)
ArchivoMenu.add_command(label="salir", command=salir)

BorrarMenu=Menu(barraMenu, tearoff=0)
BorrarMenu.add_command(label="borrar campos", command=limpiarCampos)


HerramientasMenu=Menu(barraMenu, tearoff=0)
HerramientasMenu.add_command(label="Crear registro", command=crear)
HerramientasMenu.add_command(label="Leer registro", command=leer)
HerramientasMenu.add_command(label="Editar registro", command=editar)
HerramientasMenu.add_command(label="Borar registro", command=borrar)

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia", command=licencia)
AyudaMenu.add_command(label="Proyecto", command=proyecto)

barraMenu.add_cascade(label="Archivo", menu=ArchivoMenu)
barraMenu.add_cascade(label="Borrar", menu=BorrarMenu)
barraMenu.add_cascade(label="Heramientas", menu=HerramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

# -------------desarrollo de los campos ------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miMail=StringVar()
miClave=StringVar()


#  ID 
cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

# nombre
cuadroNombre=Entry(miFrame, textvariable=miId)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="right")

# apellido
cuadroApellido=Entry(miFrame, textvariable=miNombre)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="blue", justify="right")

# direccion
cuadroDireccion=Entry(miFrame, textvariable=miApellido)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(fg="blue", justify="right")

# mail
cuadroMail=Entry(miFrame, textvariable=miMail)
cuadroMail.grid(row=4, column=1, padx=10, pady=10)
cuadroMail.config(fg="blue", justify="right")


# clave 
cuadroClave=Entry(miFrame, textvariable=miClave)
cuadroClave.grid(row=5, column=1, padx=10, pady=10)
cuadroClave.config(show="*",fg="blue", justify="right")

# comentario 
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=6, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=6, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# ........................desarrollo de los label..................

idLabel=Label(miFrame, text="Id :")
idLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre :")
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido :")
apellidoLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección :")
direccionLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

mailLabel=Label(miFrame, text="Mail :")
mailLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

claveLabel=Label(miFrame, text="Clave (hasta 10 digitos):")
claveLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario :")
comentarioLabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

# ------------------pie de cuadro ------------------------------

miFrame2=Frame(root)
miFrame2.pack()

barraFooter=Button(miFrame2, text="Copyright@ 2021 - Walter Gómez")
barraFooter.grid(row=1,column=0, sticky="e", padx=10, pady=10)





root.mainloop()