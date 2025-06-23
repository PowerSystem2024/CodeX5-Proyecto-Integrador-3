import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from usuarios import registrar_usuario, iniciar_sesion
from reservas import crear_reserva, ver_reservas, ver_todas_reservas, eliminar_reserva
from datetime import datetime, date

# Configurar tema y modo de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SistemaReservas:
    def __init__(self, root):
        self.root = root
        self.root.title("=== Sistema de Reservas Grupo CodeX5 ===")
        self.root.geometry("600x700")
        
        # Configurar estilo para Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview",
                        background="#242424",
                        foreground="#ffffff",
                        fieldbackground="#242424",
                        rowheight=25,
                        borderwidth=0)
        style.configure("Treeview.Heading",
                        background="#242424",
                        foreground="#ffffff")
        style.map("Treeview",
                  background=[('selected', '#353535'), ('active', '#353535')],
                  foreground=[('selected', '#ffffff'), ('active', '#ffffff')])
        
        self.usuario_actual = None
        self.horas = ["16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
        self.canchas = ["Fútbol", "Básquet", "Pádel"]
        
        self.mostrar_inicial()
    
    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def formatear_fecha(self, fecha):
        try:
            if isinstance(fecha, date):
                return fecha.strftime("%d/%m/%Y")
            else:
                fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
                return fecha_obj.strftime("%d/%m/%Y")
        except (ValueError, TypeError):
            return fecha
    
    def parsear_fecha(self, fecha):
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha_obj.strftime("%Y-%m-%d")
        except ValueError:
            return fecha
    
    def mostrar_inicial(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Sistema de Reservas \n\n <===|CodeX5|===>", font=("Arial", 20), text_color="#ffffff").pack(pady=20)
        ctk.CTkButton(frame, text="Registrarse", command=self.mostrar_registro, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Iniciar Sesión", command=self.mostrar_login, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Salir", command=self.root.quit, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
    
    def mostrar_registro(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Registro", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        ctk.CTkLabel(frame, text="Nombre:", text_color="#ffffff").pack()
        entrada_nombre = ctk.CTkEntry(frame, width=200, fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_nombre.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Apellido:", text_color="#ffffff").pack()
        entrada_apellido = ctk.CTkEntry(frame, width=200, fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_apellido.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Correo:", text_color="#ffffff").pack()
        entrada_correo = ctk.CTkEntry(frame, width=200, fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_correo.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Fecha de Nacimiento (dd/mm/yyyy):", text_color="#ffffff").pack()
        entrada_fecha_nac = DateEntry(
            frame,
            date_pattern="dd/mm/yyyy",
            width=20,
            background="#242424",
            foreground="#ffffff",
            selectbackground="#353535",
            selectforeground="#ffffff",
            bordercolor="#5b75f9",
            othermonthbackground="#353535"
        )
        entrada_fecha_nac.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Teléfono:", text_color="#ffffff").pack()
        entrada_telefono = ctk.CTkEntry(frame, width=200, fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_telefono.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Contraseña:", text_color="#ffffff").pack()
        entrada_contraseña = ctk.CTkEntry(frame, width=200, show="*", fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_contraseña.pack(pady=5)
        
        def registrar():
            nombre = entrada_nombre.get()
            apellido = entrada_apellido.get()
            correo = entrada_correo.get()
            fecha_nac = self.parsear_fecha(entrada_fecha_nac.get())
            telefono = entrada_telefono.get()
            contraseña = entrada_contraseña.get()
            
            if all([nombre, apellido, correo, fecha_nac, telefono, contraseña]):
                if registrar_usuario(nombre, apellido, correo, fecha_nac, telefono, contraseña):
                    messagebox.showinfo("Éxito", "Usuario registrado!")
                    self.mostrar_inicial()
                else:
                    messagebox.showerror("Error", "No se pudo registrar. El correo puede estar en uso.")
            else:
                messagebox.showerror("Error", "Complete todos los campos.")
        
        ctk.CTkButton(frame, text="Registrar", command=registrar, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_inicial, corner_radius=8, fg_color="#333333").pack(pady=20)
    
    def mostrar_login(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Iniciar Sesión", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        ctk.CTkLabel(frame, text="Correo:", text_color="#ffffff").pack()
        entrada_correo = ctk.CTkEntry(frame, width=200, fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_correo.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Contraseña:", text_color="#ffffff").pack()
        entrada_contraseña = ctk.CTkEntry(frame, width=200, show="*", fg_color="#242424", text_color="#ffffff", border_color="#5b75f9", border_width=2, corner_radius=8)
        entrada_contraseña.pack(pady=5)
        
        def login():
            correo = entrada_correo.get()
            contraseña = entrada_contraseña.get()
            if correo and contraseña:
                usuario = iniciar_sesion(correo, contraseña)
                if usuario:
                    self.usuario_actual = usuario
                    self.mostrar_menu_usuario()
                else:
                    messagebox.showerror("Error", "Correo o contraseña incorrectos.")
            else:
                messagebox.showerror("Error", "Complete todos los campos.")
        
        ctk.CTkButton(frame, text="Iniciar Sesión", command=login, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_inicial, corner_radius=8, fg_color="#333333").pack(pady=20)
    
    def mostrar_menu_usuario(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text=f"Bienvenido/a, {self.usuario_actual[1]}", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        ctk.CTkButton(frame, text="Nueva Reserva", command=self.mostrar_nueva_reserva, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Ver Reservas", command=self.mostrar_ver_reservas, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Cancelar Reserva", command=self.mostrar_cancelar_reserva, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        if self.usuario_actual[2] == 'admin':
            ctk.CTkButton(frame, text="Panel de Admin", command=self.mostrar_panel_admin, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Cerrar Sesión", command=self.mostrar_inicial, width=200, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
    
    def mostrar_nueva_reserva(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Nueva Reserva", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        ctk.CTkLabel(frame, text="Fecha (dd/mm/yyyy):", text_color="#ffffff").pack()
        entrada_fecha = DateEntry(
            frame,
            date_pattern="dd/mm/yyyy",
            width=20,
            background="#242424",
            foreground="#ffffff",
            selectbackground="#353535",
            selectforeground="#ffffff",
            bordercolor="#5b75f9",
            othermonthbackground="#353535"
        )
        entrada_fecha.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Hora:", text_color="#ffffff").pack()
        combo_hora = ctk.CTkComboBox(frame, values=self.horas, width=200, state="readonly", fg_color="#242424", text_color="#ffffff", button_color="#5b75f9", border_color="#5b75f9", border_width=2, corner_radius=8)
        combo_hora.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Cancha:", text_color="#ffffff").pack()
        combo_cancha = ctk.CTkComboBox(frame, values=self.canchas, width=200, state="readonly", fg_color="#242424", text_color="#ffffff", button_color="#5b75f9", border_color="#5b75f9", border_width=2, corner_radius=8)
        combo_cancha.pack(pady=5)
        
        def crear():
            fecha = self.parsear_fecha(entrada_fecha.get())
            hora = combo_hora.get()
            cancha = combo_cancha.get()
            if fecha and hora and cancha:
                if crear_reserva(self.usuario_actual[0], fecha, hora, cancha):
                    messagebox.showinfo("Éxito", "Reserva creada!")
                    self.mostrar_menu_usuario()
                else:
                    messagebox.showerror("Error", "El turno ya está reservado o hubo un error.")
            else:
                messagebox.showerror("Error", "Seleccione todos los campos.")
        
        ctk.CTkButton(frame, text="Crear Reserva", command=crear, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_menu_usuario, corner_radius=8, fg_color="#333333").pack(pady=20)
    
    def mostrar_ver_reservas(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Tus Reservas", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        table_frame = ctk.CTkFrame(frame, fg_color="#242424")
        table_frame.pack(fill="x", padx=10, pady=10)
        
        reservas = ver_reservas(self.usuario_actual[0])
        if reservas:
            tree = ttk.Treeview(table_frame, columns=("ID", "Fecha", "Hora", "Cancha"), show="headings", height=10)
            tree.heading("ID", text="ID")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Hora", text="Hora")
            tree.heading("Cancha", text="Cancha")
            tree.column("ID", width=50)
            tree.column("Fecha", width=100)
            tree.column("Hora", width=80)
            tree.column("Cancha", width=100)
            tree.pack(fill="x", expand=True)
            
            for reserva in reservas:
                fecha_formateada = self.formatear_fecha(reserva[1])
                tree.insert("", tk.END, values=(reserva[0], fecha_formateada, reserva[2], reserva[3]))
        else:
            ctk.CTkLabel(frame, text="No tienes reservas.", text_color="#ffffff").pack(pady=10)
        
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_menu_usuario, corner_radius=8, fg_color="#333333").pack(pady=20)
    
    def mostrar_cancelar_reserva(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Cancelar Reserva", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        table_frame = ctk.CTkFrame(frame, fg_color="#242424")
        table_frame.pack(fill="x", padx=10, pady=10)
        
        reservas = ver_reservas(self.usuario_actual[0])
        if reservas:
            tree = ttk.Treeview(table_frame, columns=("ID", "Fecha", "Hora", "Cancha"), show="headings", height=10)
            tree.heading("ID", text="ID")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Hora", text="Hora")
            tree.heading("Cancha", text="Cancha")
            tree.column("ID", width=50)
            tree.column("Fecha", width=100)
            tree.column("Hora", width=80)
            tree.column("Cancha", width=100)
            tree.pack(fill="x", expand=True)
            
            for reserva in reservas:
                fecha_formateada = self.formatear_fecha(reserva[1])
                tree.insert("", tk.END, values=(reserva[0], fecha_formateada, reserva[2], reserva[3]))
            
            def cancelar():
                seleccion = tree.selection()
                if seleccion:
                    reserva_id = tree.item(seleccion[0])["values"][0]
                    if eliminar_reserva(reserva_id):
                        messagebox.showinfo("Éxito", "Reserva cancelada!")
                        tree.delete(seleccion[0])
                    else:
                        messagebox.showerror("Error", "No se pudo cancelar la reserva.")
                else:
                    messagebox.showerror("Error", "Seleccione una reserva.")
            
            ctk.CTkButton(frame, text="Cancelar Reserva Seleccionada", command=cancelar, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        else:
            ctk.CTkLabel(frame, text="No tienes reservas.", text_color="#ffffff").pack(pady=10)
        
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_menu_usuario, corner_radius=8, fg_color="#333333").pack(pady=20)
    
    def mostrar_panel_admin(self):
        self.limpiar_frame()
        frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Panel de Administrador", font=("Arial", 16), text_color="#ffffff").pack(pady=10)
        
        ctk.CTkLabel(frame, text="Todas las Reservas", text_color="#ffffff").pack(pady=5)
        
        table_frame = ctk.CTkFrame(frame, fg_color="#242424")
        table_frame.pack(fill="x", padx=10, pady=10)
        
        reservas = ver_todas_reservas()
        if reservas:
            tree = ttk.Treeview(table_frame, columns=("ID", "UsuarioID", "Nombre", "Fecha", "Hora", "Cancha"), show="headings", height=10)
            tree.heading("ID", text="ID")
            tree.heading("UsuarioID", text="Usuario ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Hora", text="Hora")
            tree.heading("Cancha", text="Cancha")
            tree.column("ID", width=50)
            tree.column("UsuarioID", width=80)
            tree.column("Nombre", width=100)
            tree.column("Fecha", width=100)
            tree.column("Hora", width=80)
            tree.column("Cancha", width=100)
            tree.pack(fill="x", expand=True)
            
            for reserva in reservas:
                fecha_formateada = self.formatear_fecha(reserva[3])
                tree.insert("", tk.END, values=(reserva[0], reserva[1], reserva[2], fecha_formateada, reserva[4], reserva[5]))
            
            def cancelar():
                seleccion = tree.selection()
                if seleccion:
                    reserva_id = tree.item(seleccion[0])["values"][0]
                    if eliminar_reserva(reserva_id):
                        messagebox.showinfo("Éxito", "Reserva cancelada!")
                        tree.delete(seleccion[0])
                    else:
                        messagebox.showerror("Error", "No se pudo cancelar la reserva.")
                else:
                    messagebox.showerror("Error", "Seleccione una reserva.")
            
            ctk.CTkButton(frame, text="Cancelar Reserva Seleccionada", command=cancelar, corner_radius=8, fg_color="#5b75f9").pack(pady=10)
        else:
            ctk.CTkLabel(frame, text="No hay reservas.", text_color="#ffffff").pack(pady=10)
        
        ctk.CTkButton(frame, text="Volver", command=self.mostrar_menu_usuario, corner_radius=8, fg_color="#333333").pack(pady=20)

if __name__ == "__main__":
    root = ctk.CTk()
    app = SistemaReservas(root)
    root.mainloop()