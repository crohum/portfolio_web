import reflex as rx
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# Clase para agregar las imagenes de las tecnologias que conozco
class ForeachState(rx.State):
    frontend : List[str] = [
        ''
    ]

    backend : List[str] = [
        'Python',
        'MySQL'
    ]

    tools : List[str] = [
        'Markdown',
        'Git',
        'GitHub',
        'Trello',
        'Agile-Lean'
    ]


# Crea los cuadros con las imagenes de cada lista
def logos(logo: str):
    return rx.card(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src=f"techs/{logo}.png",
                        width='60px',
                        height='auto'
                    ),
                    rx.text.strong(
                        logo,
                        color='#000000'
                    ),
                    align='center'
                ),
                bg_color=Color.TERCIARIO.value,
                height="100px",
                width="100px",
                border_radius='25%'
            )
        ),
        padding=Size.DEFAULT.value,
        variant='ghost'
    )


# Funcion que se manda al main para ejecutar, Contiene los logos
def technologies():
    return rx.vstack(
        rx.heading(
            'Technologies',
            style={'font_family' : Font.TITULOS.value},
            font_size=Size.VERY_BIG.value,
            padding_top=Size.BIG.value,
            padding_bottom=Size.SMALL.value
        ),
        rx.text(
            'Backend & Database:',
            color=TextColor.SECUNDARIO.value
        ),
        rx.grid(
            rx.foreach(
                ForeachState.backend,
                logos
            ),
            columns=rx.breakpoints(initial='3', xs='4', sm='5', md='8', lg='9')
        ),
    #                           PENDIENTE HASTA QUE SEPA ALGO DE FRONT
    #    rx.text(
    #        'Frontend & Web:',
    #        color=TextColor.SECUNDARIO.value,
    #    ),
    #    rx.grid(
    #        rx.foreach(
    #            ForeachState.frontend,
    #            logos
    #        ),
    #        columns=rx.breakpoints(initial='3', xs='4', sm='5', md='8', lg='9')
    #    ),
        rx.text(
            'Tools & Methodologies:',
            color=TextColor.SECUNDARIO.value
        ),
        rx.grid(
            rx.foreach(
                ForeachState.tools,
                logos
            ),
            columns=rx.breakpoints(initial='3', xs='4', sm='5', md='8', lg='9')
        ),
        padding_bottom=Size.COLOSAL.value
    )
