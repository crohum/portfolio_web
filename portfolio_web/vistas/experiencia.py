import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# EXPERIENCE, un bloque con un resumen de mi experiencia laboral y un boton para el cv.
def experience() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Work Experience",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.PRIMARIO.value
            ),
            rx.box(
                rx.text(
                    "I started to code at April 2024, ",
                    "I'm currently looking for my first job opportunity in IT.",
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "Worked with Agile-Lean schemes (during the board ",
                    "game design workshop I collaborated in) and have implemented ",
                    "the use of Kanban boards and gamified schemes in one of my works."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "Have held positions ranging from QA, to Line Supervisor, ",
                    "to Operations Coordinator in the food industry by +17 years."
                ),
                color=TextColor.SECUNDARIO.value,
                padding=Size.MEDIUM.value
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    'See Resume',
                    href=Links.RESUME,
                    is_external=False,
                    size='3'
                ),
                rx.box(
                    rx.button(
                        'View on ',
                        rx.box(
                            class_name=f"fa fa-linkedin"
                        ),
                        size='3'
                    ),
                    href=Links.LINKEDIN_URL,
                    is_external=True
                ),
                rx.button(
                    'Download CV',
                    on_click=rx.download(url='/downloads/alejandro_garcia_salazar_cv.pdf'),
                    size='3'
                ),
                width='100%'
            )
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
