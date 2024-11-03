import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.botones import boton_footer
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text('2024'),
            rx.vstack(
                rx.text(
                    'This website was designed in Python and coded in Visual Studio Code by yours truly.',
                    as_='span'
                ),
                rx.text(
                    'Built with Reflex framework.',
                    as_='span'
                ),
                padding=Size.DEFAULT.value
            ),
            rx.spacer(),
            rx.vstack(
                rx.heading(
                    'Contact Me !',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value,
                    padding_x=Size.DEFAULT.value
                ),
                rx.hstack(
                    boton_footer(
                    'github',
                    Links.LINKEDIN_URL
                    ),
                    boton_footer(
                    'linkedin',
                    Links.LINKEDIN_URL
                    )
                )
            ),
            bg=Color.DESTACADO.value,
            padding=Size.DEFAULT.value,
            width='100%'
        )
    )
