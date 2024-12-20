import reflex as rx
import portfolio_web.componentes.enlaces as Links
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


class ForeachState(rx.State):
    proyectos : List[str] = [
        ['portfolio',
        'PORTFOLIO WEBSITE',
        "It's my first Portfolio website, build with Python using Reflex framework.",
        'https://github.com/crohum/portfolio_web'],

        ['parking',
        'PARKING MANAGEMENT',
        "A system to manage a parking lot, using the licence plate to track the time it stay at the parking lot. Also can print a stats summary of the cars parked on the day.",
        'https://github.com/crohum/parking_management'],

        ['asteroids',
        'DODGE ASTEROIDS',
        'You have to dodge the asteroids at same time to collects all stars you can. This game was build in Python with Pygame framework.',
        'https://github.com/crohum/dodge_asteroids'],

        ["invasion",
        "ALIEN's INVASION",
        'You have to destroy the aliens shot them before touch the basement, each alien destroyed respawn at random location on the top. This game was build in Python with Pygame framework.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_10'],

        ['restaurant',
        "RESTAURANT GUEST's BILL",
        "By selecting each checkbox and put the quantity consumed, the program calculates the bill's totals and prints the receipt.",
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_12'],

        ['comisiones',
        'COMMISSION CALCULATOR',
        'Calculates the commissions that correspond to each seller based on it sales. This program was build in Python with Tkinter package.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_02'],

        ['nombres',
        "NAME's CREATOR",
        'Clicking the 3 side buttons and then on generate, the program creates a fantasy name. This program was build in Python with Tkinten package.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_01'],

        ['recetas',
        "COOKBOOK",
        'A digital cookbook. This program was build in Python.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_06'],

        ['texto',
        'TEXT ANALIZER',
        'Analyzes the text and returns information about its content. This program was build in Python.',
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_03'],

        ['turnero',
        'TURN GENERATOR',
        "Generates a turn in order to wait to be attended in one of the 4 shop's areas. This program was build in Python.",
        'https://github.com/crohum/learnings_projects/tree/main/python_total/day_08']
    ]


# Crea cada bloque de cada proyecto
def cada_proyecto(proyecto: List):
    return rx.card(
        rx.box(
            rx.hstack(
                # hace que la imagen se abra en un popup
                rx.popover.root(
                    rx.popover.trigger(
                        rx.image(
                        src=f"/proyects/{proyecto[0]}.png",
                        width='250px',
                        height='auto',
                        padding_y=Size.BIG.value,
                        padding_x=Size.TINY.value
                        ),
                    ),
                    rx.popover.content(
                        rx.image(
                            src=f"/proyects/{proyecto[0]}.png",
                            #width='800px',
                            #height='auto'
                        ),
                        rx.spacer(padding_bottom=Size.DEFAULT.value),
                        rx.popover.close(
                            rx.center(
                                rx.button('Close')
                            )
                        ),
                        # rango negativo para poder centrarlo
                        align="start",
                        side_offset=-400,
                    )
                ),
                rx.vstack(
                    rx.text.strong(
                        proyecto[1],
                        color=TextColor.PRIMARIO.value
                    ),
                    rx.text(
                        proyecto[2],
                        color=TextColor.SECUNDARIO.value
                    ),
                    rx.link(
                        rx.hstack(
                            rx.text('View the code. '),
                            rx.icon('external-link')
                        ),
                        href=proyecto[3],
                        is_external=True
                    ),
                ),
                align='center'
            ),
            bg_color=Color.SECUNDARIO.value,
            height="300px",
            width="480px",
            border_radius='25px'
        ),
        padding_right=Size.VERY_BIG.value,
        padding_y=Size.BIG.value,
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
                "These are some of the programs I have coded, you can see all on my GitHub."
            ),
            bg=Color.SECUNDARIO.value,
            padding=Size.BIG.value,
            border_radius='25px',
            width='100%',
            style=MAX_WIDTH
        ),
        rx.spacer(padding=Size.BIG.value),
        rx.center(
            rx.grid(
                rx.foreach(
                    ForeachState.proyectos,
                    cada_proyecto
                ),
                columns=rx.breakpoints(sm='1', md='2')
            )
        ),
        rx.spacer(padding=Size.VERY_BIG.value),
        rx.spacer(padding=Size.COLOSAL.value),
    )
