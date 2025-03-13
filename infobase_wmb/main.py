from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('libros.db')
cursor = conn.cursor()

# Crear tabla si no existe (usando FTS para búsqueda rápida)
cursor.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS libros USING fts5(
        titulo, 
        contenido
    )
''')
conn.commit()

class MainScreen(BoxLayout):
    def buscar(self):
        texto_busqueda = self.ids.search_input.text
        cursor.execute("SELECT * FROM libros WHERE contenido MATCH ?", (texto_busqueda,))
        resultados = cursor.fetchall()
        
        # --- Parte nueva 1: Limpiar resultados viejos ---
        self.ids.resultados.clear_widgets()  # Borra todo lo anterior
        
        # --- Parte nueva 2: Crear tarjetas ---
        for res in resultados:
            titulo, contenido = res  # Extrae título y contenido
            
            # Crea un "BoxLayout" (caja) para cada tarjeta
            tarjeta = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=150,  # Altura fija para cada tarjeta
                padding=10,  # Espacio interno
                spacing=5    # Espacio entre elementos
            )
            
            # Añade color de fondo a la tarjeta (opcional)
            with tarjeta.canvas.before:
                Color(0.95, 0.95, 0.95, 1)  # Gris claro
                Rectangle(pos=tarjeta.pos, size=tarjeta.size)
            
            # Etiqueta para el título (en negrita y azul)
            titulo_label = Label(
                text=f"[b]{titulo}[/b]",  # Usa markup para negrita
                markup=True,
                size_hint_y=0.3,  # 30% de la altura de la tarjeta
                color=(0, 0, 0.5, 1)  # Color azul
            )
            
            # Etiqueta para el fragmento del contenido
            contenido_label = Label(
                text=f"{contenido[:200]}...",  # Muestra 200 caracteres
                size_hint_y=0.7,  # 70% de la altura
                color=(0.2, 0.2, 0.2, 1)  # Gris oscuro
            )
            
            # Añade las etiquetas a la tarjeta
            tarjeta.add_widget(titulo_label)
            tarjeta.add_widget(contenido_label)
            
            # Añade la tarjeta al área de resultados
            self.ids.resultados.add_widget(tarjeta)

class InfobaseApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    InfobaseApp().run()