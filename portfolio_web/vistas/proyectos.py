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
        ['portfolio', 'Portfolio Website',
        'Build in PYTHON with Reflex framework, coded in Visual Stdo Code.',
        '"This Website ^_^!"', # Es una pagina que muestra mi informacion personal como desarrollador, mi experiencia, informacion y algunos de mis proyectos realizados. Esta pagina fue creada desde cero, usando solo la documentacion oficial de Reflex como apoyo',
        'https://github.com/crohum/portfolio_web'],

        ['parking', 'Parking Management',
        'Build in PYTHON with Tkinter package, coded in PyCharm.',
        'Parking lot management to each car n day.',
        'https://github.com/crohum/parking_management'],
        
        ['asteroids', 'Dodge Asteroids',
        'Build in PYTHON with PyGame framework, coded in PyCharm.',
        'A game to dodge asteroids n collect stars.',
        'https://github.com/crohum/dodge_asteroids'],
        
        ['restaurant', "Restaurant Guest's bill",
        'Build in PYTHON with Tkinter package, coded in PyCharm.',
        "A guest's bill management.",
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_12'],
        
        ['invasion', 'Alien Invasion', 
        'Build in PYTHON with PyGame framework, coded in PyCharm.',
        'Game to shot n destroy enemies.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_10']
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
                'This is a preview, if you want see all proyects with descriptions, click "View all" ',
                color=TextColor.SECUNDARIO.value,
                padding_bottom=Size.DEFAULT.value
            ),
            # Aqui empieza el carrusel de imagenes.
            rx.center(
                rx.vstack(
                    rx.card(
                        rx.image(
                            src=f'/proyects/{State.proyectos[State.count][0]}.png',
                            width=rx.breakpoints(xs='400px', sm='500px'),
                            height='auto'
                        ),
                        height=rx.breakpoints(xs='400px', sm='500px')
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
                                rx.link(
                                    rx.heading(
                                        f"{State.proyectos[State.count][1]}",
                                        font_size="2em"
                                    ),
                                    href=State.proyectos[State.count][4],
                                    is_external=True
                                ),
                                flex_shrink='0',
                                class_name='shake',
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
                    ),
                    rx.box(
                        rx.text(
                            f'{State.proyectos[State.count][2]}',
                        ),
                        rx.text(
                            f'{State.proyectos[State.count][3]}',
                        ),
                        width=rx.breakpoints(xs='400px', sm='500px')
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
