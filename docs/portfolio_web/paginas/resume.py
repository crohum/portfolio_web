import reflex as rx
import portfolio_web.componentes.enlaces as Links
from typing import List
from portfolio_web.componentes.estilos import Font, Size, Color, TextColor, MAX_WIDTH


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
        ['Teaching / Training',
    'teach.png']
    ]

    empresas: List[str] = [
        ['LAREOCSA',
        '(DIC 2022 - JUL 2024)',
        '1 year, 8 months',
        'Area Manager'],
        ['ESTRATECNIA',
        '(OCT 2021 - OCT 2022)',
        '1 year',
        'Facilitator - Business courses'],
        ['C. Frutas Finas TARAHUMARA',
        '(SEP 2011- AGO 2021)',
        '10 years',
        'Operation Coordinator / Supervisor / Q.A.'],
        ['CENCON',
        '(JUL 2009 - MAY 2011)',
        '1 year, 10 months',
        'Quality Assurance'],
        ['GRUPO BIMBO',
        '(OCT 2005 - MAR 2009)',
        '3 years, 5 months',
        'Facilitator - Visiting guide'],
        ['BROOKLIN INSTITUTE',
        '(JAN 2001 - JUL 2002)',
        '1 year, 6 months',
        'Facilitator - Computer use, windows n office package.'],
        ['ALPEZZI CHOCOLATE',
        '(MAY 2000 - MAY 2001)',
        '1 years',
        'Quality Assurance (Intern practices)']
    ]

    actividades: List[str] = [
        ['ACTIVIDAD',
        '(1900-2000)',
        'PUESTOS']
    ]

    cursos_it: List [str] = [
        ['SQL & Bases de Datos',
        '(2024)',
        'Duracion (7 hrs)',
        'MoureDev'],
        ['git & GitHub desde cero',
        '(2024)',
        'Duracion (5 hrs)',
        'MoureDev'],
        ['Python Total',
        '(2024)',
        'Duracion (30.5 hrs)',
        'Udemy']
    ]

    cursos_varios: List [str] = [
        ['Curso basico HACCP',
        '(2021)',
        'Duracion (16 hrs)',
        'Global STD'],
        ['Narrativa y Guion de Videojuegos',
        '(2021)',
        'Duracion (30 hrs)',
        'MiriadaX / Universidad Carlos III de Madrid'],
        ['Introduccion a la Gamificacion a traves de casos practicos',
        '(2021)',
        'Duracion (26 hrs)',
        'MiriadaX / Universitat Oberta de Catalunya'],
        ['Primeros auxilios, Busqueda y rescate, Espacios confinados, Combate vs incendios, Evacuacion', '-', '-',
        'XtinFire - (2020, 2019), Santre (2015, 2014), Huntsman intl Mx (2007)'],
        ['Introduccion al diseño de videojuegos',
        '(2020)',
        'Duracion (30 hrs)',
        'MiriadaX / Fundacion Telefonica'],
        ['Gamificacion, cuando el juego se convierte en aprendizaje',
        '(2020)',
        'Duracion (24 hrs)',
        'MiriadaX / Universidad Popular Autónoma del Estado de Puebla'],
        ['Comunicacion asertiva',
        '(2019)',
        'Duracion (2 hrs)',
        'STPS Jalisco'],
        ['Persuasion y Comunicacion',
        '(2019)',
        'Duracion (2 hrs)',
        'STPS Jalisco'],
        ['Analisis y toma de decisiones',
        '(2018)',
        'Duracion (2 hrs)',
        'STPS Jalisco'],
        ['Liderazgo y trabajo en equipo',
        '(2018)',
        'Duracion (2 hrs)',
        'STPS Jalisco'],
        ['Gestion de un laboratorio de juegos',
        '(2018)', '-',
        'CCDJ - Centro de Cultura Digital Jalisco'],
        ['Supervision efectiva y manejo de personal',
        '(2017)', '-',
        'SIAZA'],
        ["Taller e implementacion 5's",
        '(2016)', '-',
        'CFF Tarahumara'],
        ['Formacion de Instructores',
        '(2016)', '-',
        'SIAZA'],
        ['Curso computacion',
        '(2001)',
        'Duracion (126 hrs)',
        'CECYTEJ #1'],
        ['Formacion humana y valores',
        '(2001)', '-',
        'CECYTEJ #1'],
        ['Desarrollo empresarial',
        '(2001)', '-',
        'CECYTEJ #1'],
        ['Encuentro de valores y educacion',
        '(1999)', '-',
        'SEJal']
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
        width='180px',
        max_width='200px'
    )


def cursos(curso: List):
    return rx.box(
        rx.card(
            rx.hstack(
                rx.text.strong(f'{curso[0]}'),
                rx.spacer(),
                rx.text(f'{curso[1]}'),
                width='100%'
            ),
            rx.text(
                f'{curso[2]}',
                align='right',
                color=TextColor.SECUNDARIO.value),
            rx.text(f'{curso[3]}'),
            bg=Color.TERCIARIO.value
        ),
        padding=Size.DEFAULT.value,
        width='340px',
        style=MAX_WIDTH
    )


def trabajos(work: List):
    return rx.box(
        rx.card(
            rx.hstack(
                rx.text.strong(f'{work[0]}'),
                rx.spacer(),
                rx.text(f'{work[1]}'),
                width='100%'
            ),
            rx.text(
                f'{work[2]}',
                align='right',
                color=TextColor.SECUNDARIO.value),
            rx.text(f'as {work[3]}')
        ),
        width='550px',
        style=MAX_WIDTH
    )


def curriculum() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Curriculum Vitae - Resume",
                        style={'font_family' : Font.TITULOS.value},
                        font_size=Size.BIG.value,
                        color=TextColor.PRIMARIO.value
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.spacer(),
                        rx.button(
                            'Download CV',
                            on_click=rx.download(url='/downloads/alejandro_garcia_salazar_cv.pdf'),
                            size='3'
                        ),
                        rx.link(
                            rx.button(
                                'View on ',
                                rx.box(
                                    class_name=f"fa fa-linkedin"
                                ),
                                size='3'
                            ),
                            href=Links.LINKEDIN_URL,
                            is_external=True   
                        )
                    ),
                    width='100%'
                ),
                rx.text(
                    "I started to code at April 2024. ",
                ),
                rx.text(
                    "I'm currently looking for my first job opportunity in IT.",
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "I Worked with Agile-Lean schemes (during the board ",
                    "game design workshop I collaborated in) and have implemented ",
                    "the use of Kanban boards and gamified schemes in one of my works as Operation Coordinator."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "Have held positions ranging from QA, to Line Supervisor, ",
                    "to Operations Coordinator in the food industry by +17 years."
                ),
                bg=Color.SECUNDARIO.value,
                padding=Size.BIG.value,
                border_radius='25px',
                width='100%',
                style=MAX_WIDTH
            ),
            rx.heading(
                "Courses",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.PRIMARIO.value,
                padding_top=Size.DEFAULT.value
            ),
            rx.grid(
                rx.foreach(
                    ForeachState.cursos_it,
                    cursos
                ),
                columns=rx.breakpoints(xs='1', sm='2', md='3')
            ),
            rx.heading(
                'Other Work Experience:',
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.PRIMARIO.value,
                padding_top=Size.VERY_BIG.value,
            ),
            rx.hstack(
                rx.heading(
                    '• By Industrial Sector',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.DESTACADO.value
                ),
                rx.text(
                    ' (years at...)',
                    style={'font_family' : Font.TITULOS.value},
                    font_size='1.5em',
                    color=TextColor.SECUNDARIO.value
                ),
                padding_top=Size.VERY_BIG.value
            ),
            rx.hstack(
                rx.foreach(
                    ForeachState.giros,
                    graficas
                )
            ),
            rx.hstack(
                rx.heading(
                    '• By Positions Helded',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.DESTACADO.value
                ),
                rx.text(
                    ' (years at...)',
                    style={'font_family' : Font.TITULOS.value},
                    font_size='1.5em',
                    color=TextColor.SECUNDARIO.value
                ),
                padding_top=Size.VERY_BIG.value
            ),
            rx.hstack(
                rx.foreach(
                    ForeachState.puestos,
                    graficas
                )
            ),
            rx.heading(
                '• By Chronological Order:',
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.DESTACADO.value,
                padding_top=Size.DEFAULT.value,
                padding_bottom=Size.SMALL.value
            ),
            rx.vstack(
                rx.foreach(
                    ForeachState.empresas,
                    trabajos
                )
            ),
            rx.heading(
                "Other Courses",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.PRIMARIO.value,
                padding_top=Size.BIG.value,
                padding_bottom=Size.DEFAULT.value
            ),
            rx.grid(
                rx.foreach(
                    ForeachState.cursos_varios,
                    cursos
                ),
                columns=rx.breakpoints(xs='1', sm='2', md='3')
            ),
            #rx.heading(
            #    'Other Activities:',
            #    style={'font_family' : Font.TITULOS.value},
            #    font_size=Size.BIG.value,
            #    color=TextColor.PRIMARIO.value,
            #    padding_top=Size.VERY_BIG.value,
            #),
            #rx.vstack(
            #    rx.foreach(
            #        ForeachState.actividades,
            #        trabajos
            #    )
            #)
        ),
        rx.spacer(padding=Size.VERY_BIG.value),
        rx.spacer(padding=Size.COLOSAL.value),
    )
