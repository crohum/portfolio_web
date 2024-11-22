import reflex as rx
import portfolio_web.componentes.enlaces as Links
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


class ForeachState(rx.State):
    proyectos : List[str] = [
        ['asteroids',
        'TITULO',
        'TEXTO'],

        ['comisiones',
        'TITULO',
        'TEXTO'],

        ['invasion',
        'TITULO',
        'TEXTO']
    ]


# Crea cada bloque de cada proyecto
def cada_proyecto(proyecto: List):
    return rx.card(
        rx.box(
            rx.hstack(
                rx.image(
                    src=f"proyects/{proyecto[0]}.png",
                    width='200px',
                    height='auto'
                ),
                rx.vstack(
                    rx.text.strong(
                        proyecto[1],
                        color=TextColor.PRIMARIO.value
                    ),
                    rx.text(
                        proyecto[2],
                        color=TextColor.SECUNDARIO.value
                    )
                ),
                align='center'
            ),
            bg_color=Color.SECUNDARIO.value,
            height="300px",
            width="500px",
            border_radius='25px'
        ),
        padding=Size.DEFAULT.value,
        variant='ghost'
    )


# El bloque que se manda al main
def proyect_page() -> rx.Component:
    return rx.box(
        rx.spacer(padding=Size.VERY_BIG),
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
                    rx.button(
                        'View all on ',
                        rx.icon(
                            'github',
                        )
                    ),
                    href=Links.GITHUB_URL,
                    is_external=True
                ),
                padding_right=Size.BIG.value,
                width='100%'
            ),
            rx.text(
                "proyectos con codigo y descripcion y asi... ",
                'texto... texto... texto... texto... texto... texto... texto... texto... texto... texto... texto... texto... texto... texto...'
            ),
            bg=Color.SECUNDARIO.value,
            padding=Size.BIG.value,
            border_radius='25px',
            style=MAX_WIDTH
        ),
        rx.spacer(padding=Size.VERY_BIG),
        rx.center(
            rx.grid(
                rx.foreach(
                    ForeachState.proyectos,
                    cada_proyecto
                ),
                columns=rx.breakpoints(sm='1', md='2')
            )
        ),
        rx.spacer(padding=Size.VERY_BIG),
        rx.spacer(padding=Size.COLOSAL),
    )
