import reflex as rx
from typing import List
from portfolio_web.componentes.estilos import Font, Size, Color, TextColor


# Todas las listas para crear los cuadros por seccion.
class ForeachState(rx.State):
    puestos : List[str] = [
    ['Operation Coordinator / Area Manager',
    'coord.png'],
    ['Supervisor',
    'supv.png'],
    ['Quality Assurance',
    'ctrqa.png'],
    ['Facilitator',
    'facilt.png']
    ]

    giros : List[str] = [
    ['Food Industry',
    'food.png'],
    ['Plastic Industry',
    'pet.png'],
    ['Teaching',
    'teach.png']
    ]


def graficas(grafica: List):
    return rx.vstack(
        rx.image(
            src=f'/graphs/{grafica[1]}',
            width='150px'
        ),
        rx.text(
            grafica[0]
        ),
        align='center',
        width='100%',
        max_width='250px'
    )


def curriculum() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text('Nada de nada en IT, pero proximamente...'),
            rx.text('Otra experiencia laboral:'),
            rx.hstack(
                rx.heading(
                    'Industrial Sector',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.text(
                    ' (years at...)',
                    style={'font_family' : Font.TITULOS.value},
                    font_size='1.5em',
                    color=TextColor.SECUNDARIO.value
                ),
                padding_top=Size.BIG.value
            ),
            rx.hstack(
                rx.foreach(
                    ForeachState.giros,
                    graficas
                )
            ),
            rx.hstack(
                rx.heading(
                    'Positions Helded',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.text(
                    ' (years at...)',
                    style={'font_family' : Font.TITULOS.value},
                    font_size='1.5em',
                    color=TextColor.SECUNDARIO.value
                ),
                padding_top=Size.BIG.value
            ),
            rx.hstack(
                rx.foreach(
                    ForeachState.puestos,
                    graficas
                )
            ),
            rx.text('CURSOS'),
            rx.text('EMPLEOS')
        ),
        rx.spacer(padding=Size.VERY_BIG.value),
        rx.spacer(padding=Size.COLOSAL.value),
    )
