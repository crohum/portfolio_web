import reflex as rx
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


def cuarentas() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "Why change to I.T. at my 40's",
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
                )
            ),
            rx.image(
                src="/otros/Turo.png",
                width="100px",
                height="auto"
            )
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )


def dolphin() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "A Dolphin (or Whale) Metaphor",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.DESTACADO.value
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
                color=TextColor.PRIMARIO.value,
                padding=Size.MEDIUM.value
            )
        ),
        bg=Color.TERCIARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
