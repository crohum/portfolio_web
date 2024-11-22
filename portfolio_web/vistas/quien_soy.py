import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# WHO AM I, Resumen corto de porque me hago desarrollador.
def who_am_i() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Who am I ?",
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.spacer(),
                rx.link(
                    rx.button('Tell me more...'),
                    href=Links.ABOUT,
                    is_external=False
                ),
                padding_right=Size.BIG.value,
                width='100%'
            ),
            rx.box(
                rx.text(
                    "My name is Alejandro Garcia Salazar aka. crohum, my first contact ",
                    "with programming world, was around 15 years old, modifying the game ",
                    "dungeon keeper's .txt, to make it more challenging, however, in my ",
                    "youth I decided to study something else."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "I am learning programming as autodidact and I'm looking for my first ",
                    "job opportunity in the IT world. I started learning Phyton, because ",
                    "I'm interested in maching learning and data science, but I would like ",
                    "to learn other backend technologies."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "Beyond work, I am passionate about board games and gamification, having ",
                    "studied some courses on the subject. ",
                    "At the moment I play TCG with my son."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "I place great importance on job stability and work-life balance in ",
                    "order to maintain creativity and well-being in my life."
                ),
                color=TextColor.SECUNDARIO.value,
                padding_bottom=Size.MEDIUM.value
            ),
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
