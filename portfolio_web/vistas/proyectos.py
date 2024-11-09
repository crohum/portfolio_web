import reflex as rx
import portfolio_web.componentes.enlaces as Links
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# Lleva el control de cual imagen mostrar tipo carrusell
class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1
        if self.count > self.maximo:
            self.count = 0

    def decrement(self):
        self.count -= 1
        if self.count < 0:
            self.count = self.maximo
    
    proyectos : List[str] = [
        '1',
        '2',
        '3',
        '4',
        '5'
    ]

    maximo : int = len(proyectos)-1


# Funcion que se manda al main para ejecutar
def proyect() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Proyects",
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.spacer(),
                rx.link(
                    rx.button('View all...'),
                    href=Links.PROYECTS,
                    is_external=False
                ),
                padding_right=Size.BIG.value,
                width='100%'
            ),
            rx.text(
                'This is a preview, if you want see all proyects, '
                'with description & code, click "View all" ',
                color=TextColor.SECUNDARIO.value,
                padding_bottom=Size.DEFAULT.value
            ),
            # Aqui empieza el carrusel de imagenes.
            rx.center(
                rx.vstack(
                    rx.card(
                        rx.image(
                            src=f'/techs/{State.proyectos[State.count]}.png',
                            width=rx.breakpoints(xs='400px', sm='500px'),
                            height='auto'
                        )
                    ),
                    rx.hstack(
                        rx.button(
                            rx.icon(
                                'arrow-big-left',
                                stroke_width=2.5,
                                color=TextColor.PRIMARIO.value
                            ),
                            on_click=State.decrement,
                        ),
                        rx.flex(
                            rx.center(
                                rx.heading(
                                    f"{State.proyectos[State.count]}",
                                    font_size="2em"
                                ),
                                flex_shrink='0',
                                width=rx.breakpoints(xs='300px', sm='400px')
                            )
                        ),
                        rx.button(
                            rx.icon(
                                'arrow-big-right',
                                stroke_width=2.5,
                                color=TextColor.PRIMARIO.value
                            ),
                            on_click=State.increment
                        ),
                        spacing="4",
                    )
                ),
                width='100%'
            )
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
