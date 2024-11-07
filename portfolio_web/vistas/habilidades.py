import reflex as rx
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# Clase para agregar las imagenes de las tecnologias que conozco
class ForeachState(rx.State):
    softskills : List[str] = [
        ''
    ]


# Crea los cuadros de la lista
def logos(logo: str):
    return


# Funcion que se manda al main para ejecutar, Contiene los logos
def skills():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    'Abilities & Softskills',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.VERY_BIG.value,
                    padding_top=Size.DEFAULT.value
                ),
                rx.text(
                    'Aqui voy a poner un grid con el logo de la skill y donde obtuve/aplique ese skill.',
                    color=TextColor.PRIMARIO.value,
                    padding_y=Size.DEFAULT.value,
                ),
                style=MAX_WIDTH
            )
        ),
        bg=Color.TERCIARIO.value,
        padding=Size.DEFAULT.value,
        width='100%'
    )
