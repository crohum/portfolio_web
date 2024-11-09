import reflex as rx
from typing import List


# Lleva el control de cual imagen mostrar
class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
    
    proyectos : List[str] = [
        ''
    ]


# Funcion que se manda al main para ejecutar
def proyect():
    return rx.box(
        
    )











"""
contador = 0
imagen display [contador]
dial 'ver codigo'
-1 boton +1
"""
